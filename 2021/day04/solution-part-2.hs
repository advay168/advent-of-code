import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

type BoardType = [[(Int, Bool)]]

parseBoard :: [String] -> BoardType
parseBoard (_ : b) = [[(read x, False) | x <- words line] | line <- b]

parseBoards :: [String] -> [BoardType]
parseBoards [] = []
parseBoards full = parseBoard (take 6 full) : parseBoards (drop 6 full)

strike :: Int -> BoardType -> BoardType
strike num board = [[(n, num == n || taken) | (n, taken) <- row] | row <- board]

isWinning :: BoardType -> Bool
isWinning board = any (all snd) board || any (all snd) (transpose board)

playGame :: [BoardType] -> [Int] -> (Int, BoardType)
playGame boards (num : nums) =
  let newBoards = map (strike num) boards
      nonWinners = filter (not . isWinning) newBoards
   in case nonWinners of
        [] -> (num, head newBoards)
        _ -> playGame nonWinners nums

score :: BoardType -> Int
score board = sum $ concat [[n | (n, taken) <- row, not taken] | row <- board]

answerFunc :: String -> Int
answerFunc all_data =
  let initial : xs = lines all_data
      nums = map read $ split ',' initial
      boards = parseBoards xs
      (num, winner) = playGame boards nums
   in score winner * num
