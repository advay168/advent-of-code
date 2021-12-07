import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

numAt :: [String] -> Int -> Int
numAt str i = if sum [if x !! i == '1' then 1 else -1 | x <- str] >= 0 then 1 else 0

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      len = length $ head lined
      counts = map (numAt lined) [0 .. (len - 1)]
      gamma = foldl (\acc x -> acc * 2 + x) 0 counts
      epsilon = 2 ^ len - 1 - gamma
   in gamma * epsilon
