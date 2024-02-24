import Data.Set qualified as S
import System.IO
import Data.List (nub)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

neighbours :: (Int, Int) -> (Int, Int) -> [(Int, Int)]
neighbours (w, h) (x, y) = filter (\(x, y) -> 0 <= x && x < w && 0 <= y && y < h) [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

next :: (Int, Int) -> S.Set (Int, Int) -> [(Int, Int)] -> [(Int, Int)]
next dims bad = nub . concatMap (filter (`S.notMember` bad) . neighbours dims)

answerFunc :: String -> Int
answerFunc all_data =
  let grid = lines all_data
      coords = concat . zipWith (\y row -> zipWith (\x c -> ((x, y), c)) [0 ..] row) [0 ..] $ grid
      bad = S.fromList . map fst . filter ((== '#') . snd) $ coords
      start = fst . head . filter ((== 'S') . snd) $ coords
      stepped = iterate (next (length grid, length $ head grid) bad) [start]
   in length $ stepped !! 64
