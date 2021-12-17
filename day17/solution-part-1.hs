import Data.List
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

xAt :: Int -> Int -> Int
xAt vel step' =
  let sign = signum vel
      abs_vel = abs vel
      step = min step' vel
   in (abs_vel * step - step * (step - 1) `div` 2) * sign

yAt :: Int -> Int -> Int
yAt vel step = vel * step - step * (step - 1) `div` 2

maxY :: Int -> Int
maxY vel = vel * (vel + 1) `div` 2

willIntersect :: ((Int, Int), (Int, Int)) -> (Int -> Int) -> (Int -> Int) -> Bool
willIntersect ((xMin, xMax), (yMin, yMax)) xFunc yFunc =
  let isValid step = and [xMin <= xFunc step, xFunc step <= xMax, yMin <= yFunc step, yFunc step <= yMax]
      shouldContinue step = xFunc step <= xMax && yFunc step >= yMin
   in foldr (\step rest -> shouldContinue step && (isValid step || rest)) False [0 .. 400]

answerFunc :: String -> Int
answerFunc all_data =
  let Just line = stripPrefix "target area: " $ head $ lines all_data
      (_ : _ : xRange, _ : _ : _ : _ : yRange) = break (== ',') line
      (xMin', _ : _ : xMax') = break (== '.') xRange
      (yMin', _ : _ : yMax') = break (== '.') yRange
      (xMin : xMax : yMin : yMax : _) = map read [xMin', xMax', yMin', yMax']
      intersects xVel yVel = willIntersect ((xMin, xMax), (yMin, yMax)) (xAt xVel) (yAt yVel)
   in maximum [maxY yVel | xVel <- [0 .. xMax + 1], yVel <- [0 .. abs yMin], intersects xVel yVel]
