import Data.List (nub)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Pos = (Int, Int)

data State = State Pos Pos [Pos]

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      initState = State (0, 0) (0, 0) []
      State _ tailPos visited = foldl parseAndMove initState lined
   in length . nub $ tailPos:visited

moveTailTowardsHead :: State -> State
moveTailTowardsHead state@(State (hx, hy) (tx, ty) visited) = case (abs (hx - tx) == 2, abs (hy - ty) == 2) of
  (False, True) -> State (hx, hy) (hx, ty + signum (hy - ty)) ((tx, ty) : visited)
  (True, False) -> State (hx, hy) (tx + signum (hx - tx), hy) ((tx, ty) : visited)
  _ -> state

move :: State -> Pos -> State
move (State (hx, hy) (tx, ty) visited) (dhx, dhy) = moveTailTowardsHead $ State (hx + dhx, hy + dhy) (tx, ty) visited

parseAndMove :: State -> String -> State
parseAndMove state line = case words line of
  ["U", num] -> foldl move state $ replicate (read num) (0, 1)
  ["D", num] -> foldl move state $ replicate (read num) (0, -1)
  ["R", num] -> foldl move state $ replicate (read num) (1, 0)
  ["L", num] -> foldl move state $ replicate (read num) (-1, 0)
