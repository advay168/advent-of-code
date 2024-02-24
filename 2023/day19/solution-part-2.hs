import Data.List (foldl')
import Data.Map qualified as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Part = P {x :: (Int, Int), m :: (Int, Int), a :: (Int, Int), s :: (Int, Int)}

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

get :: Char -> Part -> (Int, Int)
get 'x' = x
get 'm' = m
get 'a' = a
get 's' = s

modify :: Char -> Part -> (Int, Int) -> Part
modify 'x' part val = part {x = val}
modify 'm' part val = part {m = val}
modify 'a' part val = part {a = val}
modify 's' part val = part {s = val}

allOfPart :: Part -> Int
allOfPart (P (x0, x1) (m0, m1) (a0, a1) (s0, s1)) = (x1 - x0 + 1) * (m1 - m0 + 1) * (a1 - a0 + 1) * (s1 - s0 + 1)

numAcceptable :: M.Map String ([(Op, Char, Int, String)], String) -> String -> Part -> Int
numAcceptable workflows current part =
  let (conds, last) = workflows M.! current
      f (s, part) (op, var, val, next) = case op of
        '<' -> (numAcceptable workflows next (modify var part (minn, val - 1)) + s, modify var part (val, maxx))
        '>' -> (numAcceptable workflows next (modify var part (val + 1, maxx)) + s, modify var part (minn, val))
        where
          (minn, maxx) = get var part
      (count, part') = foldl f (0, part) conds
   in case current of
        "A" -> allOfPart part
        "R" -> 0
        _ -> count + numAcceptable workflows last part'

answerFunc :: String -> Int
answerFunc all_data =
  let workflows = M.fromList . map parseWorkflow . takeWhile (/= "") . lines $ all_data
   in numAcceptable workflows "in" $ P (1, 4000) (1, 4000) (1, 4000) (1, 4000)
