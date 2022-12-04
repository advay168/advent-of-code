main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
   in length . filter enclosed . map extract $ lined 

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

extract :: String -> (Int, Int, Int, Int)
extract str =
  let [[a, b], [c, d]] = map (split '-') (split ',' str)
   in (read a, read b, read c, read d)

enclosed :: (Int, Int, Int, Int) -> Bool
enclosed (a, b, c, d)
  | a < c = d <= b
  | a == c = True
  | otherwise = enclosed (c, d, a, b)
