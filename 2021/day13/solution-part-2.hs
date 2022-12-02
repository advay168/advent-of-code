import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  mapM putStrLn $ answerFunc all_data

type Point = (Int, Int)

parseFold :: String -> Point -> Point
parseFold line (x, y) =
  let Just removed = stripPrefix "fold along " line
      (axis, _ : val) = break (== '=') removed
      foldPos = read val
   in if axis == "x"
        then (foldPos - abs (x - foldPos), y)
        else (x, foldPos - abs (y - foldPos))

parsePoint :: String -> Point
parsePoint line = let (x, _ : y) = break (== ',') line in (read x, read y)

parseLines :: [String] -> ([Point], [Point -> Point])
parseLines [] = ([], [])
parseLines (line : xs)
  | line == "" = (points, folds)
  | "fold" `isPrefixOf` line = (points, parseFold line : folds)
  | otherwise = (parsePoint line : points, folds)
  where
    (points, folds) = parseLines xs

answerFunc :: String -> [String]
answerFunc all_data =
  let lined = lines all_data
      (points, folds) = parseLines lined
      finalPoints = foldl (flip map) points folds
      maxX = maximum $ map fst finalPoints
      maxY = maximum $ map snd finalPoints
      emptyGrid = replicate (maxY + 1) (replicate (maxX + 1) ' ')
      increment grid (x, y) = take y grid ++ [take x row ++ ['@'] ++ drop (x + 1) row] ++ drop (y + 1) grid where row = grid !! y
   in foldl increment emptyGrid finalPoints
