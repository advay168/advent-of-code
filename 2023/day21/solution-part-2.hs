import Data.Set qualified as S
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

next :: (Int, Int) -> S.Set (Int, Int) -> S.Set (Int, Int) -> S.Set (Int, Int)
next (w, h) bad = S.foldl' go S.empty
  where
    f (x, y) = filter (\(x, y) -> S.notMember (x `mod` w, y `mod` h) bad) [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    go acc = S.union acc . S.fromList . f

answerFunc :: String -> Int
answerFunc all_data =
  let grid = lines all_data
      coords = concat . zipWith (\y row -> zipWith (\x c -> ((x, y), c)) [0 ..] row) [0 ..] $ grid
      bad = S.fromList . map fst . filter ((== '#') . snd) $ coords
      start = fst . head . filter ((== 'S') . snd) $ coords
      dims@(w, _) = (length grid, length $ head grid)
      stepped = iterate (next dims bad) $ S.fromList [start]
      n = 26501365
      [y0, y1, y2] = map (length . (stepped !!)) . take 3 . iterate (+ w) $ (n `mod` w)
      a = ((y2 - c) `div` 2) - (y1 - c)
      b = y1 - (a + c)
      c = y0
      x = n `div` w
   in a * x * x + b * x + c
