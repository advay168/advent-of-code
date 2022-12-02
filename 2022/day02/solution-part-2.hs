import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      split = map (\[abc, ' ', xyz] -> (abc, xyz)) lined
   in sum . map (score . uncurry convert) $ split

convert 'A' 'X' = ('A', 'Z')
convert 'B' 'X' = ('B', 'X')
convert 'C' 'X' = ('C', 'Y')
convert 'A' 'Y' = ('A', 'X')
convert 'B' 'Y' = ('B', 'Y')
convert 'C' 'Y' = ('C', 'Z')
convert 'A' 'Z' = ('A', 'Y')
convert 'B' 'Z' = ('B', 'Z')
convert 'C' 'Z' = ('C', 'X')

score (abc, xyz) = scoreXYZ xyz + scoreAll abc xyz

scoreXYZ 'X' = 1
scoreXYZ 'Y' = 2
scoreXYZ 'Z' = 3

scoreAll 'A' 'Z' = 0
scoreAll 'B' 'X' = 0
scoreAll 'C' 'Y' = 0
scoreAll 'A' 'X' = 3
scoreAll 'B' 'Y' = 3
scoreAll 'C' 'Z' = 3
scoreAll 'A' 'Y' = 6
scoreAll 'B' 'Z' = 6
scoreAll 'C' 'X' = 6
