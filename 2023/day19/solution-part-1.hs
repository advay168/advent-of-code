import Data.List (foldl')
import Data.Map qualified as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Part = P {x :: Int, m :: Int, a :: Int, s :: Int} deriving (Read)

type Op = Char

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

upto1 [] = []
upto1 [_] = []
upto1 (a : b : xs) = a : upto1 (b : xs)

parseWorkflow :: String -> (String, ([(Op, Char, Int, String)], String))
parseWorkflow line =
  let [name, rest] = split '{' line
      conditions' = split ',' $ upto1 rest
      conditions = upto1 conditions'
      parseCond cond' =
        let [cond, goto] = split ':' cond'
            [[var1], val1] = split '<' cond
            [[var2], val2] = split '>' cond
         in if '<' `elem` cond
              then ('<', var1, read val1, goto)
              else ('>', var2, read val2, goto)
   in (name, (map parseCond conditions, last conditions'))

parsePart :: String -> Part
parsePart = read . ('P' :)

get :: Char -> Part -> Int
get 'x' = x
get 'm' = m
get 'a' = a
get 's' = s

checkPart :: M.Map String ([(Op, Char, Int, String)], String) -> String -> Part -> Bool
checkPart workflows current part =
  let (conds, last) = workflows M.! current
      f (op, var, val, next) (worked, status) = case op of
        '<' -> if get var part < val then (True, checkPart workflows next part) else (worked, status)
        '>' -> if get var part > val then (True, checkPart workflows next part) else (worked, status)
      (worked, status) = foldr f (False, False) conds
   in case current of
        "A" -> True
        "R" -> False
        _ -> if worked then status else checkPart workflows last part

scorePart :: Part -> Int
scorePart (P x m a s) = x + m + a + s

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (workflows', _ : parts') = break (== "") lined
      workflows = M.fromList $ map parseWorkflow workflows'
      parts = map parsePart parts'
      accepted = filter (checkPart workflows "in") parts
   in sum . map scorePart $ accepted
