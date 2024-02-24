import Data.Bifunctor (first, second)
import Data.List (foldl')
import Numeric (readHex)
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

upto1 [] = []
upto1 [_] = []
upto1 (a : b : xs) = a : upto1 (b : xs)

parseLine :: String -> (Char, Int)
parseLine line =
  let [_, _, _ : _ : cs] = words line
      n = upto1 . upto1 $ cs
      d = last . upto1 $ cs
   in (d, fst . head $ readHex n)

go :: (Int, Int) -> (Char, Int) -> (Int, Int)
go pos ('0', n) = first (+ n) pos
go pos ('1', n) = second (+ n) pos
go pos ('2', n) = first (subtract n) pos
go pos ('3', n) = second (subtract n) pos

area :: [(Int, Int)] -> Int
area points = (abs a + b) `div` 2 + 1
  where
    (a, b) =
      foldl' (\(asum, bsum) (a, b) -> (asum + a, bsum + b)) (0, 0)
        $ zipWith
          (\(x0, y0) (x1, y1) -> (x0 * y1 - x1 * y0, abs (x1 - x0) + abs (y1 - y0)))
          points
        $ tail points ++ [head points]

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      plan = map parseLine lined
      points = scanl go (0, 0) plan
   in area points
