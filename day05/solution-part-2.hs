import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Point = (Int, Int)

type Line = (Point, Point)

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

parseLine :: String -> Line
parseLine l =
  let [p1, _, p2] = words l
      [x1, y1] = split ',' p1
      [x2, y2] = split ',' p2
   in ((read x1, read y1), (read x2, read y2))

allPointsFromLine :: Line -> [Point]
allPointsFromLine ((x1, y1), (x2, y2))
  | x1 == x2 && y1 == y2 = []
  | otherwise = (newx, newy) : allPointsFromLine ((newx, newy), (x2, y2))
  where
    newx = x1 + signum (x2 - x1)
    newy = y1 + signum (y2 - y1)

allPoints :: [Line] -> [Point]
allPoints lines = concatMap allPointsFromLine lines ++ map fst lines

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      allLines = map parseLine lined
   in length . filter (> 1) . map length . group . sort $ allPoints allLines
