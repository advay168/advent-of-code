import Data.Bifunctor (bimap)
import Data.List (sort)
import Data.Map qualified as M
import Data.Maybe (fromMaybe)
import System.IO

data Module = FlipFlop {connected :: [String], fState :: Bool} | Conjunction {connected :: [String], cState :: [(String, Bool)]}
type State = M.Map String Module
type ToProcess = [(String, String, Bool)]

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

parseLine :: String -> (String, [String])
parseLine line = let (name : _ : rest) = words line in (name, map (filter (/= ',')) rest)

initConjunctions :: State -> State
initConjunctions modules = M.foldlWithKey go modules modules
  where
    go modified name =
      let modifier (Conjunction connected st) = Conjunction connected $ (name, False) : st
          modifier x = x
       in foldr (M.update $ Just . modifier) modified . connected

step :: ToProcess -> State -> (ToProcess, State)
step xs state = (xs, state)

runButtonPress :: State -> State
runButtonPress modules = modules

-- answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (broadcaster : modules) = map parseLine . reverse . sort $ lined
      (nands, flipfs) =
        bimap
          (map $ bimap tail $ flip Conjunction [])
          (map $ bimap tail $ flip FlipFlop False)
          $ break ((== '%') . head . fst) modules
      mods' = M.fromList $ nands ++ flipfs
      mods = initConjunctions mods'
   in broadcaster
