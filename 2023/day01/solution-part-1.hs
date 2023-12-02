import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map extract lined
   in sum . map (\lst -> read (head lst:[last lst])) $ parsed

extract :: String -> [Char]
extract "" = []
extract (x:xs) = if x `elem` ['0'..'9'] then x:extract xs else extract xs
