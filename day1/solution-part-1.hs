import System.IO

--
main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let (initial : rest) = map (read :: String -> Int) (lines all_data)
      ans =
        foldl
          (\(count, prev) x -> (if x > prev then count + 1 else count, x))
          (0, initial)
          rest
   in fst ans
