import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Point = (Int, Int)

parseFold :: String -> Point -> Point
parseFold line (x, y) =
  let Just removed = stripPrefix "fold along " line
      (axis, _ : val) = break (== '=') removed
      intVal = read val
   in if axis == "x"
        then (intVal - abs (x - intVal), y)
        else (x, intVal - abs (y - intVal))

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

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (points, folds) = parseLines lined
   in length . nub . map (head folds) $ points
