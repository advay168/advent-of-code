import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

next :: Bool -> Int -> (Int, Int, Int, Int) -> (Int, Int, Int, Int)
next p1Turn t (pos1, pos2, score1, score2) =
  if p1Turn
    then (newPos1, pos2, score1 + newPos1, score2)
    else (pos1, newPos2, score1, score2 + newPos2)
  where
    rollSum = (t + (t + 1) + (t + 2)) `mod` 100 + 2
    newPos1 = (pos1 + rollSum) `mod` 10 + 1
    newPos2 = (pos2 + rollSum) `mod` 10 + 1

generateStates :: Bool -> Int -> (Int, Int, Int, Int) -> [((Int, Int, Int, Int), Int)]
generateStates turn t state = (state, t) : generateStates (not turn) (t + 3) (next turn t state)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (_, _ : p1) = break (== ':') $ head lined
      (_, _ : p2) = break (== ':') $ lined !! 1
      (pos1, pos2) = (read p1, read p2)
      states = generateStates True 0 (pos1, pos2, 0, 0)
      Just ((_, _, s1, s2), t) = find (\((_, _, s1, s2), _) -> s1 >= 1000 || s2 >= 1000) states
   in min s1 s2 * t
