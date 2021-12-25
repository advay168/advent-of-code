import Data.List (intercalate)
import qualified Data.Map as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Expr
  = Cst Int
  | Expr :+ Expr
  | Expr :* Expr
  | Expr :/ Expr
  | Expr :% Expr
  | Expr :== Expr
  | Inp Int
  deriving (Show)

type State = (Expr, Expr, Expr, Expr, [Expr])

replace :: State -> String -> Expr -> State
replace (w, x, y, z, constraints) "w" expr = (expr, x, y, z, constraints)
replace (w, x, y, z, constraints) "x" expr = (w, expr, y, z, constraints)
replace (w, x, y, z, constraints) "y" expr = (w, x, expr, z, constraints)
replace (w, x, y, z, constraints) "z" expr = (w, x, y, expr, constraints)

addConstraint :: State -> Expr -> State
addConstraint (w, x, y, z, constraints) expr = (w, x, y, z, expr : constraints)

getExpr :: State -> String -> Expr
getExpr (w, x, y, z, _) "w" = w
getExpr (w, x, y, z, _) "x" = x
getExpr (w, x, y, z, _) "y" = y
getExpr (w, x, y, z, _) "z" = z

aluAdd' :: State -> String -> String -> State
aluAdd' state a b =
  if b `elem` ["w", "x", "y", "z"]
    then aluAdd (getExpr state a) (getExpr state b)
    else aluAdd (getExpr state a) (Cst (read b))
  where
    aluAdd :: Expr -> Expr -> State
    expr_a `aluAdd` (Cst 0) = replace state a expr_a
    (Cst 0) `aluAdd` expr_b = replace state a expr_b
    (Cst val1) `aluAdd` (Cst val2) = replace state a (Cst (val1 + val2))
    (expr :+ (Cst val1)) `aluAdd` (Cst val2) = replace state a (expr :+ Cst (val1 + val2))
    expr_a `aluAdd` expr_b = replace state a (expr_a :+ expr_b)

aluMul' :: State -> String -> String -> State
aluMul' state a b =
  if b `elem` ["w", "x", "y", "z"]
    then aluMul (getExpr state a) (getExpr state b)
    else aluMul (getExpr state a) (Cst (read b))
  where
    aluMul :: Expr -> Expr -> State
    expr_a `aluMul` (Cst 1) = replace state a expr_a
    expr_a `aluMul` (Cst 0) = replace state a (Cst 0)
    (Cst 0) `aluMul` expr_b = replace state a (Cst 0)
    (Cst 1) `aluMul` expr_b = replace state a expr_b
    expr_a `aluMul` expr_b = replace state a (expr_a :* expr_b)

aluMod' :: State -> String -> String -> State
aluMod' state a b =
  if b `elem` ["w", "x", "y", "z"]
    then aluMod (getExpr state a) (getExpr state b)
    else aluMod (getExpr state a) (Cst (read b))
  where
    aluMod :: Expr -> Expr -> State
    (Cst 0) `aluMod` expr_b = replace state a (Cst 0)
    ((Inp _) :+ (Cst val)) `aluMod` (Cst modulus) | modulus > val + 9 = state
    ((_ :* (Cst val1)) :+ expr) `aluMod` (Cst val2) | val1 == val2 = replace state a expr
    expr_a `aluMod` expr_b = replace state a (expr_a :% expr_b)

aluDiv' :: State -> String -> String -> State
aluDiv' state a b =
  if b `elem` ["w", "x", "y", "z"]
    then aluDiv (getExpr state a) (getExpr state b)
    else aluDiv (getExpr state a) (Cst (read b))
  where
    aluDiv :: Expr -> Expr -> State
    (Cst 0) `aluDiv` expr_b = replace state a (Cst 0)
    expr_a `aluDiv` (Cst 1) = replace state a expr_a
    ((expr :* (Cst val1)) :+ _) `aluDiv` (Cst val2) | val1 == val2 = replace state a expr
    ((Inp _) :+ (Cst val1)) `aluDiv` (Cst val2) | val1 + 10 < val2 = replace state a (Cst 0)
    expr_a `aluDiv` expr_b = replace state a (expr_a :/ expr_b)

aluEql' :: State -> String -> String -> State
aluEql' state a b =
  if b `elem` ["w", "x", "y", "z"]
    then aluEql (getExpr state a) (getExpr state b)
    else aluEql (getExpr state a) (Cst (read b))
  where
    aluEql :: Expr -> Expr -> State
    (Cst val) `aluEql` (Inp _) | val >= 10 = replace state a (Cst 0)
    (Inp _) `aluEql` (Cst val) | val >= 10 = replace state a (Cst 0)
    ((Inp _) :+ (Cst val)) `aluEql` (Inp _) | val >= 10 = replace state a (Cst 0)
    (Cst val1) `aluEql` (Cst val2) = replace state a (Cst (fromEnum (val1 == val2)))
    -- Assumption
    lhs@((Inp inp1) :+ expr) `aluEql` rhs@(Inp inp2) = addConstraint (replace state a (Cst 1)) (lhs :== rhs)
    expr_a `aluEql` expr_b = replace state a (expr_a :== expr_b)

parseLine :: (State, [Int]) -> [String] -> (State, [Int])
parseLine (state, next : inps) ["inp", a] = (replace state a (Inp next), inps)
parseLine (state, inps) ["add", a, b] = (aluAdd' state a b, inps)
parseLine (state, inps) ["mul", a, b] = (aluMul' state a b, inps)
parseLine (state, inps) ["div", a, b] = (aluDiv' state a b, inps)
parseLine (state, inps) ["mod", a, b] = (aluMod' state a b, inps)
parseLine (state, inps) ["eql", a, b] = (aluEql' state a b, inps)

-- Assumption
simplifyConstraints :: State -> [(Int, Int, Int)]
simplifyConstraints (_, _, _, _, constraints) =
  map
    (\(((Inp b) :+ (Cst c)) :== (Inp a)) -> (a, b, c))
    constraints

applyConstraint :: (Int, Int, Int) -> M.Map Int Int -> M.Map Int Int
applyConstraint (a, b, c) digits =
  if c >= 0
    then M.adjust (const 9) a $ M.adjust (const (9 - c)) b digits
    else M.adjust (const (val + c)) a digits
  where
    val = digits M.! b

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      initialState = ((Cst 0, Cst 0, Cst 0, Cst 0, []), [1 .. 14])
      (constraints, _) = foldl parseLine initialState $ map words lined
      simplified = simplifyConstraints constraints
      initialDigits = M.fromList [(digit, 9) | digit <- [1 .. 14]]
   in foldl (\num digit -> num * 10 + digit) 0 . M.elems . foldr applyConstraint initialDigits $ simplified
