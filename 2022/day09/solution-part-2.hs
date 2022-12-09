import Data.List (nub)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Pos = (Int, Int)

data State = State [Pos] [Pos]

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      initState = State (replicate 10 (0, 0)) []
      State knots visited = foldl parseAndMove initState lined
   in length . nub $ visited

moveTailTowardsHead :: Pos -> Pos -> Pos
moveTailTowardsHead (hx, hy) (tx, ty) = case (abs (hx - tx) > 1, abs (hy - ty) > 1) of
  (True, True) -> (tx + signum (hx - tx), ty + signum (hy - ty))
  (False, True) -> (hx, ty + signum (hy - ty))
  (True, False) -> (tx + signum (hx - tx), hy)
  (False, False) -> (tx, ty)

move :: State -> Pos -> State
move (State ((hx, hy) : rest) visited) (dhx, dhy) = State newKnots (last newKnots : visited)
  where
    newKnots = scanl1 moveTailTowardsHead ((hx + dhx, hy + dhy) : rest)

parseAndMove :: State -> String -> State
parseAndMove state line = case words line of
  ["U", num] -> foldl move state $ replicate (read num) (0, 1)
  ["D", num] -> foldl move state $ replicate (read num) (0, -1)
  ["R", num] -> foldl move state $ replicate (read num) (1, 0)
  ["L", num] -> foldl move state $ replicate (read num) (-1, 0)
