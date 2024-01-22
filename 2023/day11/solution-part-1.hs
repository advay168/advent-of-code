import Data.Bool (bool)
import Data.List (foldl', transpose)
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Cell = Empty | Galaxy deriving (Eq)

parse :: [String] -> [[Cell]]
parse = map (map (\c -> if c == '.' then Empty else Galaxy))

findEmptyRows :: [[Cell]] -> [Int]
findEmptyRows = map fst . filter (all (== Empty) . snd) . zip [0 ..]

findGalaxies :: [[Cell]] -> [(Int, Int)]
findGalaxies = concat . zipWith (\y row -> (map (\(x, _) -> (x, y)) . filter ((== Galaxy) . snd)) $ zip [0 ..] row) [0 ..]

distFunc :: [[Cell]] -> ((Int, Int), (Int, Int)) -> Int
distFunc grid = f
  where
    emptyRows = findEmptyRows grid
    dpRows = scanl (+) 0 $ map (\y -> bool 1 2 (y `elem` emptyRows)) [0 ..]
    emptyCols = findEmptyRows (transpose grid)
    dpCols = scanl (+) 0 $ map (\x -> bool 1 2 (x `elem` emptyCols)) [0 ..]
    oneD checkList (a, b) =
      let (start, end) = (min a b, max a b)
       in (checkList !! end) - (checkList !! start)
    f ((x0, y0), (x1, y1)) = oneD dpCols (x0, x1) + oneD dpRows (y0, y1)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      grid = parse lined
      galaxies = findGalaxies grid
      dist = distFunc grid
   in sum [dist (a, b) | a <- galaxies, b <- galaxies, a < b]
