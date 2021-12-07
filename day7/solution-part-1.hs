import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

parseList :: String -> [Int]
parseList str = read $ "[" ++ str ++ "]"

cost :: [Int] -> Int -> Int
cost positions pos = sum $ map (abs . (pos -)) positions

answerFunc :: String -> Int
answerFunc all_data =
  let l = parseList $ head $ lines all_data
   in minimum $ map (cost l) l
