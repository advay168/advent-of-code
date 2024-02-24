import Data.Char (ord)
import Data.List (foldl')
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

hash :: String -> Int
hash = foldl' (\h c -> (h + ord c) * 17 `mod` 256) 0

answerFunc :: String -> Int
answerFunc all_data =
  let [line] = lines all_data
   in sum . map hash . split ',' $ line
