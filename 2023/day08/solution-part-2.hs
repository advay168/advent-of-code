import Data.List (foldl1', isSuffixOf)
import Data.Map qualified as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Graph = M.Map String (String, String)

parseLine :: String -> (String, (String, String))
parseLine line = let [node, l, r] = words $ filter (not . (`elem` "=(,)")) line in (node, (l, r))

nextOf :: Graph -> (String, String) -> (String, String)
nextOf graph (dir : directions, current) = (directions, if dir == 'L' then fst possibles else snd possibles)
  where
    possibles = graph M.! current

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      directions : _ : nodes = lined
      graph = M.fromList . map parseLine $ nodes
      locations initial = iterate (nextOf graph) (cycle directions, initial)
   in foldl1 lcm . map (length . takeWhile (not . isSuffixOf "Z" . snd) . locations) . filter (isSuffixOf "A") $ M.keys graph
