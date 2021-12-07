import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

action :: (Int, Int) -> (String, Int) -> (Int, Int)
action (forward, depth) ("forward", amount) = (forward + amount, depth)
action (forward, depth) ("down", amount) = (forward, depth + amount)
action (forward, depth) ("up", amount) = (forward, depth - amount)

answerFunc :: String -> Int
answerFunc text =
  let lined = map (\str -> let arguments = words str in (head arguments, read $ arguments !! 1)) (lines text)
      (forward, depth) = foldl action (0, 0) lined
   in forward * depth
