import Data.Char (isLower)
import Data.Tuple
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

countPaths :: [(String, String)] -> [String] -> Bool -> String -> Int
countPaths edges seen ok current
  | current == "end" = 1
  | otherwise =
    let newSeen = if all isLower current then current : seen else seen
        present = current `elem` seen
     in if present && not ok
          then 0
          else sum . map (countPaths edges newSeen (not present && ok) . snd) . filter ((== current) . fst) $ edges

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      x = map (\line -> let (a, _ : b) = break (== '-') line in (a, b)) lined
      edges' = x ++ map swap x
      edges = filter ((/= "end") . fst) . filter ((/= "start") . snd) $ edges'
   in countPaths edges [] True "start"
