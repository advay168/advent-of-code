import Data.List (groupBy)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

-- oneliner = maximum . map (sum . map read . tail) . groupBy (\a b -> b /= "") . ("" :) . lines . init

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      broken = calcSum lined
   in maximum broken

calcSum :: [String] -> [Int]
calcSum xs = map (sum . map read . tail) . groupBy (\_ x -> x /= "") $ "" : xs
