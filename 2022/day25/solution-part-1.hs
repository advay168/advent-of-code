main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> String
answerFunc all_data =
  let lined = lines all_data
      s = sum . map sToD $ lined
   in dToS s

sToD :: String -> Int
sToD = foldl helper 0
  where
    helper s '0' = s * 5 + 0
    helper s '1' = s * 5 + 1
    helper s '2' = s * 5 + 2
    helper s '-' = s * 5 - 1
    helper s '=' = s * 5 - 2

dToS :: Int -> String
dToS = reverse . helper
  where
    helper 0 = ""
    helper x =
      case x `mod` 5 of
        0 -> '0' : helper (div (x - 0) 5)
        1 -> '1' : helper (div (x - 1) 5)
        2 -> '2' : helper (div (x - 2) 5)
        3 -> '=' : helper (div (x + 2) 5)
        4 -> '-' : helper (div (x + 2) 5)
