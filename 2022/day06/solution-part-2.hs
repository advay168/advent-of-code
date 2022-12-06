import Data.List (nub)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let groups = groupIntoN 14 all_data 1
      unique = filter uniqueFilter groups
   in snd $ head unique

groupIntoN :: Int -> String -> Int -> [([Char], Int)]
groupIntoN n lst idx = (take n lst, idx + n - 1) : groupIntoN n (tail lst) (idx + 1)

uniqueFilter :: ([Char], Int) -> Bool
uniqueFilter (lst, _) = lst == nub lst
