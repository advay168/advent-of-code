import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

action :: (Int, Int, Int) -> (String, Int) -> (Int, Int, Int)
action (forward, depth, aim) ("forward", amount) = (forward + amount, depth + amount * aim, aim)
action (forward, depth, aim) ("down", amount) = (forward, depth, aim + amount)
action (forward, depth, aim) ("up", amount) = (forward, depth, aim - amount)

answerFunc :: String -> Int
answerFunc text =
  let lined = map (\str -> let arguments = words str in (head arguments, read $ arguments !! 1)) (lines text)
      (forward, depth, _) = foldl action (0, 0, 0) lined
   in forward * depth
