import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

predict :: [Int] -> Int
predict nums =
  let diffs = zipWith (-) (tail nums) nums
   in if all (== 0) diffs then last nums else last nums + predict diffs

parseLine :: String -> [Int]
parseLine line = map read $ words line

answerFunc :: String -> Int
answerFunc = sum . map (predict . parseLine) . lines
