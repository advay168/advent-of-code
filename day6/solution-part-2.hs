import Data.Array
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

type Table = Array Int Int

fishes' :: Int -> Table -> (Int, Table)
fishes' num_days table
  | num_days <= 0 = (1, table)
  | otherwise =
    let val = 1 + sum [fst $ fishes' (num_days - i) table | i <- [9, 16 .. num_days + 8]]
     in if (table ! num_days) /= -1 then (table ! num_days, table) else (val, table // [(num_days, val)])

fishes :: Int -> Int -> Table -> (Int, Table)
fishes sum' num_days table = (val + sum', new_table)
  where
    (val, new_table) = fishes' num_days table

answerFunc :: String -> Int
answerFunc all_data =
  let nums = map read $ split ',' all_data
      days = 256
      reduced = map (days -) nums
      initialTable = listArray (0, days + 1) [-1, -1 ..]
      computedTable = foldl (\table num_days -> snd $ fishes' num_days table) initialTable [0 .. days + 1]
   in sum $ map (computedTable !) reduced
