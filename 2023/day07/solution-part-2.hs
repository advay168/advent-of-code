import Data.List (nub, sort, sortOn)
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

parseLine :: String -> (String, Int)
parseLine line = let [a, b] = words line in (a, read b)

counts :: String -> [Int]
counts str = [length . filter (x ==) $ str | x <- nub str]

translate :: String -> String
translate "" = ""
translate ('A' : xs) = 'Z' : translate xs
translate ('K' : xs) = 'Y' : translate xs
translate ('Q' : xs) = 'X' : translate xs
translate ('J' : xs) = '0' : translate xs
translate ('T' : xs) = 'V' : translate xs
translate (x : xs) = x : translate xs

key :: String -> ([Int], String)
key hand =
  let js = length . filter (== 'J') $ hand
      removed = filter (/= 'J') hand
      inc [] = [5]
      inc (x : xs) = x + js : xs
      new = inc . reverse . sort . counts $ removed
   in (new, translate hand)

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map parseLine lined
      ranked = zip [1 ..] $ sortOn (key . fst) parsed
      mul (rank, (_, bid)) = rank * bid
   in sum . map mul $ ranked
