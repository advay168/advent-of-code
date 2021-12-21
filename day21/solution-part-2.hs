import Data.List
import qualified Data.Map as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

weightOf :: Int -> Int
weightOf 3 = 1
weightOf 4 = 3
weightOf 5 = 6
weightOf 6 = 7
weightOf 7 = 6
weightOf 8 = 3
weightOf 9 = 1

type State = (Int, Int, Int, Int, Bool)

winnings :: M.Map State (Int, Int) -> State -> ((Int, Int), M.Map State (Int, Int))
winnings cache state@(pos1, pos2, score1, score2, p1Turn)
  | Just retVal <- M.lookup state cache = (retVal, cache)
  | score1 >= 21 = ((1, 0), M.insert state (1, 0) cache)
  | score2 >= 21 = ((0, 1), M.insert state (0, 1) cache)
  | otherwise =
    let newPos1 i = (pos1 + i - 1) `mod` 10 + 1
        newPos2 i = (pos2 + i - 1) `mod` 10 + 1
        (calc, newCache) =
          if p1Turn
            then
              foldl
                ( \((wins1, wins2), cache) i ->
                    let ((w1, w2), newCache) = winnings cache (newPos1 i, pos2, score1 + newPos1 i, score2, not p1Turn)
                     in ((wins1 + w1 * weightOf i, wins2 + w2 * weightOf i), newCache)
                )
                ((0, 0), cache)
                [3 .. 9]
            else
              foldl
                ( \((wins1, wins2), cache) i ->
                    let ((w1, w2), newCache) = winnings cache (pos1, newPos2 i, score1, score2 + newPos2 i, not p1Turn)
                     in ((wins1 + w1 * weightOf i, wins2 + w2 * weightOf i), newCache)
                )
                ((0, 0), cache)
                [3 .. 9]
     in (calc, M.insert state calc newCache)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (_, _ : p1) = break (== ':') $ head lined
      (_, _ : p2) = break (== ':') $ lined !! 1
      (pos1, pos2) = (read p1, read p2)
   in uncurry max . fst $ winnings M.empty (pos1, pos2, 0, 0, True)
