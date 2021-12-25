import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

xyToIdx :: (Int, Int) -> (Int, Int) -> Int
xyToIdx (width, height) (x, y) = y * width + x

idxToXy :: (Int, Int) -> Int -> (Int, Int)
idxToXy (width, height) idx = (mod idx width, div idx width)

isValidIndex :: (Int, Int) -> (Int, Int) -> Bool
isValidIndex (width, height) (x, y) = and [x >= 0, x < width, y >= 0, y < height]

getNeighbours :: (Int, Int) -> Int -> [Int]
getNeighbours dim idx =
  map (xyToIdx dim) $ filter (isValidIndex dim) [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
  where
    (x, y) = idxToXy dim idx

isLowPoint :: (Int, Int) -> [Int] -> Int -> Bool
isLowPoint dim grid idx = all (((grid !! idx) <) . (grid !!)) (getNeighbours dim idx)

findLowPoints :: (Int, Int) -> [Int] -> [Int]
findLowPoints dim grid = filter (isLowPoint dim grid) [0 .. length grid - 1]

answerFunc :: String -> Int
answerFunc all_data =
  let grid' = map (map (read . (: []))) $ lines all_data
      width = length (head grid')
      height = length grid'
      grid = concat grid'
   in sum . map ((+ 1) . (grid !!)) $ findLowPoints (width, height) grid
