import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

solve :: Int -> Int -> Int
solve time record = sum [1 | t <- [0..time-1], t * (time - t) > record]

answerFunc :: String -> Int
answerFunc all_data =
  let [t, d] = lines all_data
      times = map read . tail $ words t
      dists = map read . tail $ words d
   in product $ zipWith solve times dists

