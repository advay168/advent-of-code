import Data.List (groupBy, foldl', minimumBy)
import System.IO
import Data.Function (on)

main = do
  all_data <- readFile "./input.txt"
  print $ answerFunc all_data

data Range = Range
  { start :: Int,
    end :: Int,
    offset :: Int
  }

type Mapper = [Range]

type Seed = Range

parseSeeds :: [String] -> [Seed]
parseSeeds [] = []
parseSeeds (source:length:seeds) = Range (read source) (read source + read length) 0: parseSeeds seeds

parseRange :: String -> Range
parseRange line = let [dest, src, len] = map read $ words line in Range {start = src, end = src + len, offset = dest - src}

parseMapper :: [String] -> Mapper
parseMapper = map parseRange

parse :: [String] -> ([Seed], [Mapper])
parse (seeds : maps) =
  ( parseSeeds . tail $ words seeds,
    map (parseMapper . drop 2) $ groupBy (\_ b -> b /= "") maps
  )

transformSeeds'' :: Seed -> Range -> [Seed]
transformSeeds'' (Range seedStart seedEnd orig) (Range rangeStart rangeEnd offset)
  | seedEnd <= rangeStart   = [Range seedStart seedEnd orig]
  | rangeEnd <= seedStart   = [Range seedStart seedEnd orig]
  | rangeStart <= seedStart && seedEnd <= rangeEnd = [Range seedStart seedEnd offset]
  | rangeStart <= seedStart = [Range seedStart rangeEnd offset, Range rangeEnd seedEnd orig]
  | seedEnd <= rangeEnd     = [Range seedStart rangeStart orig, Range rangeStart seedEnd offset]
  | otherwise               = [Range seedStart rangeStart orig, Range rangeStart rangeEnd offset, Range rangeEnd seedEnd orig]

addSeed :: Seed -> Seed
addSeed (Range start end offset) = Range (start + offset) (end + offset) 0

transformSeeds' :: [Seed] -> Mapper -> [Seed]
transformSeeds' = foldl' (\seeds r -> concatMap (`transformSeeds''` r) seeds)

transformSeeds :: [Seed] -> [Mapper] -> [Seed]
transformSeeds = foldl' ((map addSeed .) . transformSeeds')

answerFunc :: String -> Int
answerFunc all_data =
  let lined = lines all_data
      (seeds, maps) = parse lined
   in start . minimumBy (compare `on` start) $ transformSeeds seeds maps
