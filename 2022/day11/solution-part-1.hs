import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
   in 0

