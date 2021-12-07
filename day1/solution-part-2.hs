import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lst = map (read :: String -> Int) (lines all_data)
      (initial : rest) = zipWith3 (\x y z -> x + y + z) lst (drop 1 lst) (drop 2 lst)
      ans =
        foldl
          (\(count, prev) x -> (if x > prev then count + 1 else count, x))
          (0, initial)
          rest
   in fst ans
