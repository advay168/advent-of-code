import Data.Map qualified as M
import System.IO

type Coord = (Int, Int)

type Grid = [String]

type Ix = (Coord, Coord)

type Cache = M.Map Ix [Coord]

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

width :: Grid -> Int
width (row : _) = length row

height :: Grid -> Int
height = length

(</>) :: Cache -> Coord -> (Cache, [Coord])
(<\>) :: Cache -> Coord -> (Cache, [Coord])
(<|>) :: Cache -> Coord -> (Cache, [Coord])
(<->) :: Cache -> Coord -> (Cache, [Coord])
(<.>) :: Cache -> Coord -> (Cache, [Coord])

cache </> dir = (cache, [])

cache <\> dir = (cache, [])

cache <|> dir = (cache, [])

cache <-> dir = (cache, [])

cache <.> dir = (cache, [])

{-
 - energise
 - Parameters:
 -  cache of (pos, dir) -> path
 -  grid
 -  (pos, dir)
 - Returns
 -  cache with (pos, dir) filled and some more
 -  [Ix] path filled
 - -}


energise :: Cache -> Grid -> Ix -> (Cache, [Coord])
energise cache grid k@((px, py), dir)
  | M.member k cache = (cache, cache M.! k)
  | px < 0 || w <= px = (cache, [])
  | py < 0 || h <= py = (cache, [])
  | otherwise = case (grid !! py) !! px of
      '/' -> cache </> dir
      '\\' -> cache <\> dir
      '|' -> cache <|> dir
      '-' -> cache <-> dir
      '.' -> cache <.> dir
  where
    w = width grid
    h = height grid

answerFunc :: String -> Int
answerFunc all_data =
  let grid = lines all_data
   in 0
