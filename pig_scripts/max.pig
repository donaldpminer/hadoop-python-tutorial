
register '/home/python/pig_scripts/udfs.py' using streaming_python as pyudfs;

A = LOAD '/home/python/data/salarydata/' USING TextLoader() as (line:chararray);

B = FOREACH A GENERATE pyudfs.extract_dollar(line) as pay:int, line;

C = ORDER B BY pay DESC;

D = LIMIT C 15;

dump D;
