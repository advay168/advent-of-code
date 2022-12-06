import Data.List (nub)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let unique = filter uniqueFilter $ groupIntoN 4 all_data 1
   in snd $ head unique

groupIntoN :: Int -> String -> Int -> [([Char], Int)]
groupIntoN n lst idx = (take n lst, idx + n - 1) : groupIntoN n (tail lst) (idx + 1)

uniqueFilter :: ([Char], Int) -> Bool
uniqueFilter (lst, _) = lst == nub lst
