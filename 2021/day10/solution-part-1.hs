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
score ')' = 3
score ']' = 57
score '}' = 1197
score '>' = 25137
score ' ' = 0

unexpected :: String -> String -> Char
unexpected _ "" = ' '
unexpected [] (char : line) = unexpected [matchingBracket char] line
unexpected (expected : xs) (char : line)
  | char `elem` "([{<" = unexpected (matchingBracket char : expected : xs) line
  | char == expected = unexpected xs line
  | otherwise = char

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
   in sum . map (score . unexpected []) $ lined
