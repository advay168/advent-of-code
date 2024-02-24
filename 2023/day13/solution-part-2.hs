import Control.Applicative ((<|>))
import Data.List (find, groupBy, transpose)
import Data.Maybe (fromJust)
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

parseGrids :: [String] -> [[String]]
parseGrids = map tail . groupBy (\_ b -> b /= "") . ("" :)

count :: String -> String -> Int
count a b = length . filter id $ zipWith (/=) a b

isReflection :: ([String], [String]) -> Bool
isReflection (a, b) = (== 1) . sum $ zipWith count b (reverse a)

groupings :: [String] -> [([String], [String])]
groupings grid = map (`splitAt` grid) [1 .. length grid - 1]

score' :: [String] -> Maybe Int
score' grid = length . fst <$> find isReflection (groupings grid)

score :: [String] -> Maybe Int
score grid = ((100 *) <$> score' grid) <|> score' (transpose grid)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      grids = parseGrids lined
   in sum . map (fromJust . score) $ grids
