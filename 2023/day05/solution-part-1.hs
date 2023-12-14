import Data.List (groupBy, foldl')
import System.IO

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Range = Range
  { start :: Int,
    end :: Int,
    offset :: Int
  }

type Mapper = [Range]

type Seed = Int

parseRange :: String -> Range
parseRange line = let [dest, src, len] = map read $ words line in Range {start = src, end = src + len, offset = dest - src}

parseMapper :: [String] -> Mapper
parseMapper = map parseRange

parse :: [String] -> ([Seed], [Mapper])
parse (seeds : maps) =
  ( map read . tail $ words seeds,
    map (parseMapper . drop 2) $ groupBy (\_ b -> b /= "") maps
  )

within :: Seed -> Range -> Bool
within seed (Range start end _) = start <= seed && seed < end

transformSeed' :: Seed -> Mapper -> Seed
transformSeed' seed = foldr (\range mapped -> if seed `within` range then seed + offset range else mapped) seed

transformSeed :: [Mapper] -> Seed -> Seed
transformSeed = flip $ foldl' transformSeed'

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (seeds, maps) = parse lined
   in minimum $ map (transformSeed maps) seeds
