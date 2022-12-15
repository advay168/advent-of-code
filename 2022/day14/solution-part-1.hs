import qualified Data.Map as M
import Data.Maybe (fromMaybe, isNothing)
import Data.List (find)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Pos = (Int, Int)

data Cell = Empty | Rock | Sand deriving (Eq, Show)

type State = (M.Map Pos Cell, Pos)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      full = concatMap separate lined
      state = createInitState full
      (a, c) = runToCompletetion state
   in subtract 2 . length . filter ((== Sand) . snd) . M.toList $ a


simulateStep :: State -> (Bool, Bool, Pos) -- (stopped, bounded, state)
simulateStep state@(grid, sandPos) = (any (`M.notMember` grid) n , isNothing newPos, fromMaybe (500, 0) newPos)
  where
    neighbours (x, y) = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
    n = neighbours sandPos
    helper pos = case M.lookup pos grid of
      Just Empty -> True
      Just Rock -> False
      Just Sand -> False
      Nothing -> False
    newPos = find helper n

simulate :: State -> (Bool, State)
simulate state@(grid, sandPos) =
  let (stopped, bounded, newPos) = simulateStep state
   in if bounded || stopped then (stopped, (M.insert sandPos Sand grid, newPos)) else simulate (grid, newPos)

runToCompletetion :: State -> State
runToCompletetion state = case simulate state of
  (True, newState) -> newState
  (False, newState) -> runToCompletetion newState

parseNumbers :: String -> [Pos]
parseNumbers str = map (parsePair . break (== ',')) . everySecond . words $ "-> " ++ str
  where
    everySecond [] = []
    everySecond (_ : b : xs) = b : everySecond xs
    parsePair (a, _ : b) = (read a, read b)

separate :: String -> [(Pos, Pos)]
separate str =
  reverse $
    foldl
      (\(lastPair@(_, lastCoord) : rest) currentPos -> (lastCoord, currentPos) : lastPair : rest)
      [(head parsed, head parsed)]
      (tail parsed)
  where
    parsed = parseNumbers str

calcBounds :: [(Pos, Pos)] -> (Pos, Pos)
calcBounds lst = ((minimumX, 0), (maximumX, maximumY))
  where
    minimumX = minimum . map (fst . snd) $ lst
    maximumX = maximum . map (fst . snd) $ lst
    maximumY = maximum . map (snd . snd) $ lst

createInitState :: [(Pos, Pos)] -> State
createInitState lst = (M.insert (500, 0) Sand (foldl helper initGrid lst), (500, 0))
  where
    b@((miX, miY), (maX, maY)) = calcBounds lst
    initGrid = foldl (\grid coord -> M.insert coord Empty grid) M.empty [(x, y) | x <- [miX .. maX], y <- [miY .. maY]]
    enumerate :: (Pos, Pos) -> [Pos]
    enumerate ((ax, ay), (bx, by))
      | ax == bx = [(ax, y) | y <- [(min ay by) .. (max ay by)]]
      | ay == by = [(x, ay) | x <- [(min ax bx) .. (max ax bx)]]
    helper grid coords =
      foldl
        (\g coord -> M.insert coord Rock g)
        grid
        (enumerate coords)
