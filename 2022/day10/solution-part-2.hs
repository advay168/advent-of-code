import Data.List

main = do
  all_data <- readFile "./input.txt"
  putStrLn $ answerFunc all_data

answerFunc :: String -> String
answerFunc all_data =
  let lined = lines all_data
      initState = [1]
      positions = map spritePositionSpan . reverse . foldl parseAndDo initState $ map words lined
      combined = zipWith elem (map cpuPosition [0 ..]) positions
   in intercalate "\n" . split40 $ draw combined

parseAndDo :: [Int] -> [String] -> [Int]
parseAndDo (first : rest) ["noop"] = first : first : rest
parseAndDo (first : rest) [_, val] = (first + read val) : first : first : rest

spritePositionSpan :: Int -> [Int]
spritePositionSpan x = [x - 1, x, x + 1]

cpuPosition :: Int -> Int
cpuPosition x = x `mod` 40

draw :: [Bool] -> String
draw = map (\x -> if x then '#' else ' ')

split40 :: String -> [String]
split40 [] = []
split40 list = first : split40 rest
  where
    (first, rest) = splitAt 40 list
