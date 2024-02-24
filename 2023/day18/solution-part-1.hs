import Data.Bifunctor (first, second)
import Data.List (foldl')
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

parseLine :: String -> (Char, Int)
parseLine line = let [[dir], n, _] = words line in (dir, read n)

go :: (Int, Int) -> (Char, Int) -> (Int, Int)
go pos ('U', n) = second (subtract n) pos
go pos ('D', n) = second (+ n) pos
go pos ('L', n) = first (subtract n) pos
go pos ('R', n) = first (+ n) pos

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
