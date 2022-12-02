import Data.List
import Numeric
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

matchingBracket :: Char -> Char
matchingBracket '(' = ')'
matchingBracket '[' = ']'
matchingBracket '{' = '}'
matchingBracket '<' = '>'

score :: Char -> Int
score ')' = 1
score ']' = 2
score '}' = 3
score '>' = 4

unexpected :: String -> String -> String
unexpected [] "" = " "
unexpected xs "" = xs
unexpected [] (char : line) = unexpected [matchingBracket char] line
unexpected (expected : xs) (char : line)
  | char `elem` "([{<" = unexpected (matchingBracket char : expected : xs) line
  | char == expected = unexpected xs line
  | otherwise = " "

median :: [Int] -> Int
median xs = sort xs !! (length xs `div` 2)

answerFunc :: String -> Int
answerFunc = median . map (fst . head . readInt 5 (const True) score) . filter (/= " ") . map (unexpected []) . lines
