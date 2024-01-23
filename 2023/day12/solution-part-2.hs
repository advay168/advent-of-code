import Control.Monad (foldM)
import Control.Monad.State.Strict (State, evalState, get, gets, modify', unless)
import Data.List (intercalate)
import Data.Map.Strict qualified as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

parseLine :: String -> (String, [Int])
parseLine line =
  let [report, rle] = words line
   in (intercalate "?" (replicate 5 report) ++ ".", concat . replicate 5 . map read $ split ',' rle)

solve :: (String, [Int]) -> State (M.Map (String, [Int], Int) Int) Int
solve (!report, !rle) =
  let helper ("", [], 0) = return 1
      helper ("", _, _) = return 0
      helper inp@(r : report, rle, currentRun) =
        do
          let calculated = do
                x <- if r == '.' then return 0 else helper (report, rle, currentRun + 1)
                y <- case (r, rle, currentRun) of
                  ('#', _, _) -> return 0
                  (_, _, 0) -> helper (report, rle, 0)
                  (_, r : rle, currentRun) | r == currentRun -> helper (report, rle, 0)
                  _ -> return 0
                modify' $ M.insert inp (x + y)
                return (x + y)
          gets (M.lookup inp) >>= maybe calculated return
   in helper (report, rle, 0)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map parseLine lined
      solved = foldM (\acc inp -> (acc +) <$> solve inp) 0 parsed
   in evalState solved M.empty
