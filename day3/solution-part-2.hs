import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

numAt :: (Int -> Bool) -> [String] -> Int -> Char
numAt func str i = if func $ sum [if x !! i == '1' then 1 else -1 | x <- str] then '1' else '0'

filterPossibles :: [String] -> (Int -> Bool) -> Int -> String
filterPossibles [x] _ _ = x
filterPossibles possibles func i = filterPossibles (filter (\x -> x !! i == target) possibles) func (i + 1)
  where
    target = numAt func possibles i

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      o2 = foldl (\acc x -> acc * 2 + read [x]) 0 $ filterPossibles lined (>= 0) 0
      co2 = foldl (\acc x -> acc * 2 + read [x]) 0 $ filterPossibles lined (< 0) 0
   in o2 * co2
