import Data.Char (ord)
import Data.Foldable (toList)
import Data.List (foldl')
import Data.Sequence qualified as S
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

type Boxes = S.Seq [(String, Char)]

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

hash :: String -> Int
hash = foldl' (\h c -> (h + ord c) * 17 `mod` 256) 0

upto1 [] = []
upto1 [_] = []
upto1 (a : b : xs) = a : upto1 (b : xs)

delete :: Boxes -> String -> Boxes
delete boxes word =
  let label = upto1 word
      h = hash label
   in S.adjust' (filter ((/= label) . fst)) h boxes

update :: Boxes -> String -> Boxes
update boxes word =
  let label = upto1 $ upto1 word
      d = last word
      h = hash label
      f [] = [(label, d)]
      f ((l, d') : bs) = if l == label then (label, d) : bs else (l, d') : f bs
   in S.adjust' f h boxes

transform :: Boxes -> String -> Boxes
transform boxes word =
  if last word == '-'
    then delete boxes word
    else update boxes word

answerFunc :: String -> Int
answerFunc all_data =
  let [line] = lines all_data
      initial = S.replicate 256 []
      final = foldl transform initial . split ',' $ line
   in sum . map sum $
        zipWith (\i box -> zipWith (\j (_, d) -> i * j * read [d]) [1 ..] box) [1 ..] $
          toList final
