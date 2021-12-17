import qualified Data.Map as M
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Counts = M.Map String Int

type Rules = M.Map String (String, String)

parseRules :: [String] -> Rules -> Rules
parseRules [] original = original
parseRules (line : xs) original = parseRules xs $ M.insert key val original
  where
    [key@[char1, char2], _, [character]] = words line
    val = ([char1, character], [character, char2])

getCount :: String -> Counts
getCount template = foldr (\(char1, char2) counts -> M.insertWith (+) [char1, char2] 1 counts) M.empty $ zip template (tail template)

nextCounts :: Rules -> Counts -> Counts
nextCounts rules =
  M.foldlWithKey
    ( \newCounts pair count ->
        let (a, b) = rules M.! pair
         in M.insertWith (+) a count $ M.insertWith (+) b count newCounts
    )
    M.empty

performNSteps :: Int -> Rules -> Counts -> Counts
performNSteps 0 _ counts = counts
performNSteps numSteps rules counts = performNSteps (numSteps - 1) rules (nextCounts rules counts)

getLetterCounts :: Counts -> M.Map Char Int
getLetterCounts =
  M.foldlWithKey
    (\newCounts [char1, char2] count -> M.insertWith (+) char1 count $ M.insertWith (+) char2 count newCounts)
    M.empty

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      template = head lined
      rules = parseRules (drop 2 lined) M.empty
      counts = getCount template
      numSteps = 40
      finalCounts = performNSteps numSteps rules counts
      letterCounts = M.insertWith (+) (last template) 1 . M.insertWith (+) (head template) 1 $ getLetterCounts finalCounts
   in (maximum letterCounts - minimum letterCounts) `div` 2
