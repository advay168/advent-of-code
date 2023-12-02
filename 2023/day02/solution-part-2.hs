import Data.List (foldl')
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

split :: Char -> String -> [String]
split delimeter xs = case break (== delimeter) xs of
  (word, "") -> [word]
  (word, _ : rs) -> word : split delimeter rs

parse :: String -> (Int, [(Int, Int, Int)])
parse line =
  let [gn, rest] = split ':' line
      [_, n] = words gn
      rounds = map (split ',') . split ';' $ rest
      tuplise [n, colour] = (read n, colour)
      convert (r, g, b) (n, colour) =
        ( if colour == "red" then n else r,
          if colour == "green" then n else g,
          if colour == "blue" then n else b
        )
      rgbs = map (foldl' convert (0, 0, 0) . map (tuplise . words)) rounds
   in (read n, rgbs)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map (snd . parse) lined
      maxRGB (r1, g1, b1) (r2, g2, b2) = (max r1 r2, max g1 g2, max b1 b2)
      prodRGB (r, g, b) = r * g * b
   in sum . map (prodRGB . foldl' maxRGB (0, 0, 0)) $ parsed
