import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      out = map (\line -> let (_, _ : x) = break (== '|') line in x) lined
      flattened = concatMap words out
      filtered = filter ((`elem` [2, 3, 4, 7]) . length) flattened
   in length filtered
