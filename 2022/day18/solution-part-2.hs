import qualified Data.Set as S

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Point = (Int, Int, Int)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map parse lined
      maxD = maxDim parsed + 2
      cubes = S.fromList parsed
   in count cubes maxD

neighbours :: Int -> Point -> [Point]
neighbours maxD (x, y, z) =
  filter
    (\(a, b, c) -> -2 <= a && a < maxD && -2 <= b && b < maxD && -2 <= c && c < maxD)
    [ (x - 1, y, z),
      (x + 1, y, z),
      (x, y - 1, z),
      (x, y + 1, z),
      (x, y, z - 1),
      (x, y, z + 1)
    ]

dfs :: S.Set Point -> Int -> S.Set Point -> Point -> (Int, S.Set Point)
dfs cubes maxD visited current =
  foldl
    func
    (0, S.insert current visited)
    (neighbours maxD current)
  where
    func (count, visited) neighbour =
      let (a, newV) = dfs cubes maxD visited neighbour
       in if neighbour `S.member` visited
            then (count, visited)
            else (if neighbour `S.member` cubes then (count + 1, visited) else (count + a, newV))

count :: S.Set Point -> Int -> Int
count cubes maxD = fst $ dfs cubes maxD S.empty (0, 0, 0)

parse :: String -> Point
parse str =
  let helper ',' = ' '
      helper c = c
      [a, b, c] = words $ map helper str
   in (read a, read b, read c)

maxDim :: [Point] -> Int
maxDim lst = maximum [maximum (map _1 lst), maximum (map _2 lst), maximum (map _3 lst)]
  where
    _1 (x, _, _) = x
    _2 (_, _, x) = x
    _3 (_, _, x) = x
