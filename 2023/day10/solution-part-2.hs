import Data.List (find, foldl')
import Data.Map qualified as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Coord = (Int, Int)

type Graph = M.Map Coord (Coord, Coord)

parseMap :: M.Map (Int, Int) Char -> Graph
parseMap = M.mapWithKey $ \(x, y) c -> case c of
  '-' -> ((x - 1, y), (x + 1, y))
  '|' -> ((x, y - 1), (x, y + 1))
  'L' -> ((x, y - 1), (x + 1, y))
  'J' -> ((x, y - 1), (x - 1, y))
  '7' -> ((x, y + 1), (x - 1, y))
  'F' -> ((x, y + 1), (x + 1, y))
  _ -> ((-1, -1), (-1, -1))

area :: [(Int, Int)] -> Int
area points = (abs a - b) `div` 2 + 1
  where
    (a, b) =
      foldl' (\(asum, bsum) (a, b) -> (asum + a, bsum + b)) (0, 0)
        $ zipWith
          (\(x0, y0) (x1, y1) -> (x0 * y1 - x1 * y0, abs (x1 - x0) + abs (y1 - y0)))
          points
        $ tail points ++ [head points]

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      grid = concat $ zipWith (\line row -> zipWith (\cell col -> ((col, row), cell)) line [0 ..]) lined [0 ..]
      graph = parseMap $ M.fromList grid
      Just (start, _) = find ((== 'S') . snd) grid
      Just nextNode = M.foldrWithKey (\coord (a, b) acc -> if start `elem` [a, b] then Just coord else acc) Nothing graph
      findPath :: Coord -> [Coord] -> [Coord]
      findPath current path
        | current == start = path
        | otherwise =
            let (a, b) = graph M.! current
             in findPath (if head path == a then b else a) (current:path)
      path = findPath nextNode [start]
   in area path
