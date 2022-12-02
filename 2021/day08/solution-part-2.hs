import Data.List
import qualified Data.Map as M
import Data.Maybe
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

mapping =
  [ "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
  ]

charToIndex :: Char -> Int
charToIndex chr = fromEnum chr - fromEnum 'a'

indexToChar :: Int -> Char
indexToChar num = toEnum (num + fromEnum 'a')

common :: [String] -> String
common = foldr1 intersect

notN :: Int -> String
notN n = "abcdefg" \\ common (filter ((== n) . length) mapping)

type Grid = [[Bool]]

replaceFalse :: Grid -> Int -> Int -> Grid
replaceFalse grid y x = take y grid ++ [take x row ++ [False] ++ drop (x + 1) row] ++ drop (y + 1) grid where row = grid !! y

crossOutChar :: Int -> Grid -> Char -> Grid
crossOutChar len grid char =
  let xs = map charToIndex $ notN len
      index = charToIndex char
      f grid = replaceFalse grid index
   in foldl f grid xs

crossOutLength :: [String] -> Grid -> Int -> Grid
crossOutLength signals grid len = foldl (crossOutChar len) grid (common . filter ((== len) . length) $ signals)

crossOut :: [String] -> Grid
crossOut signals = foldl (crossOutLength signals) (replicate 7 (replicate 7 True)) [2, 3, 4, 5, 6]

fillColumn :: Grid -> Int -> Grid
fillColumn grid col = foldl (\grid i -> replaceFalse grid i col) grid [0 .. 6]

findRow :: Grid -> Int
findRow grid = foldr (\(i, row) index -> if filter (== True) row == [True] then i else index) undefined $ zip [0 ..] grid

findTable :: Grid -> M.Map Char Char -> (Grid, M.Map Char Char)
findTable grid table =
  let solvableIndex = findRow grid
      Just location = elemIndex True (grid !! solvableIndex)
   in if length table == 7
        then (grid, table)
        else findTable (fillColumn grid location) (M.insert (indexToChar solvableIndex) (indexToChar location) table)

decodeDigit :: M.Map Char Char -> String -> Int
decodeDigit table digit = fromJust $ sort (map (\c -> fromJust $ M.lookup c table) digit) `elemIndex` mapping

decodeNum :: M.Map Char Char -> [String] -> Int
decodeNum table digits = foldl (\num digit -> num * 10 + digit) 0 $ map (decodeDigit table) digits

solveLine :: (String, String) -> Int
solveLine (input, output) =
  let grid = crossOut $ words input
      (_, table) = findTable grid M.empty
   in decodeNum table (words output)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      splitted = map (\line -> let (a, _ : b) = break (== '|') line in (a, b)) lined
   in sum . map solveLine $ splitted
