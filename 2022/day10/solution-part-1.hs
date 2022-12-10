main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      initState = [1, 0]
      finalState = reverse . foldl parseAndDo initState $ map words lined
      interestingIndices = [20, 60 .. length finalState -1]
      interestingValues = map (\idx -> idx * (finalState !! idx)) interestingIndices
   in sum interestingValues

parseAndDo :: [Int] -> [String] -> [Int]
parseAndDo (first : rest) ["noop"] = first : first : rest
parseAndDo (first : rest) [_, val] = (first + read val) : first : first : rest
