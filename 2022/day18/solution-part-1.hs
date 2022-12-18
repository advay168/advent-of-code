import qualified Data.Set as S

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Point = (Int, Int, Int)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map parse lined
      cubes = S.fromList parsed
   in sum $ map (count cubes) parsed

neighbours :: Point -> [Point]
neighbours (x, y, z) =
  [ (x - 1, y, z),
    (x + 1, y, z),
    (x, y - 1, z),
    (x, y + 1, z),
    (x, y, z - 1),
    (x, y, z + 1)
  ]

count :: S.Set Point -> Point -> Int
count cubes cube = sum $ map (\v -> if v `S.member` cubes then 0 else 1) $ neighbours cube

parse :: String -> Point
parse str =
  let helper ',' = ' '
      helper c = c
      [a, b, c] = words $ map helper str
   in (read a, read b, read c)
