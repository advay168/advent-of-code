import Data.List (groupBy, sortOn)
import Data.Ord (Down (Down))

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

-- oneliner = sum . take 3 . sortOn Down . map (sum . map read . tail) . groupBy (\a b -> b /= "") . ("" :) . lines . init

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      broken = calcSum lined
   in sum . take 3 . sortOn Down $ broken

calcSum :: [String] -> [Int]
calcSum xs = map (sum . map read . tail) . groupBy (\_ x -> x /= "") $ "" : xs
