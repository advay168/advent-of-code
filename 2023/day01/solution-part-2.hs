import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      parsed = map extract lined
   in sum . map (\lst -> read (head lst:[last lst])) $ parsed

extract :: String -> [Char]
extract "" = []
extract xs@('o':'n':'e'        :_) = '1':extract (tail xs)
extract xs@('t':'w':'o'        :_) = '2':extract (tail xs)
extract xs@('t':'h':'r':'e':'e':_) = '3':extract (tail xs)
extract xs@('f':'o':'u':'r'    :_) = '4':extract (tail xs)
extract xs@('f':'i':'v':'e'    :_) = '5':extract (tail xs)
extract xs@('s':'i':'x'        :_) = '6':extract (tail xs)
extract xs@('s':'e':'v':'e':'n':_) = '7':extract (tail xs)
extract xs@('e':'i':'g':'h':'t':_) = '8':extract (tail xs)
extract xs@('n':'i':'n':'e'    :_) = '9':extract (tail xs)
extract (x:xs)                     = if x `elem` ['0'..'9'] then x:extract xs else extract xs
