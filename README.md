# File splitter/reassembler

This is a quick Python/Bash pair of programs I wrote to split a large file into smaller chunks, and then reassemble those chunks later on. 

# Usage

## Splitter

To split a file, run `python split_file_chunks.py $filepath $chunkSize` where `$filepath` is the path to the file you want to split, and `$chunkSize` is a positive integer representing the size of the chunks it will create, in megabytes. 

The output is n "chunk" files, where n is the size of the original file in bytes divided by `$chunkSize` megabytes. The chunk files follow the naming convention `$originalName`_`$chunkNumber`, where `$originalName` is the name of the file passed into the program, and `$chunkNumber` is the chunk's index, i.e. what position it belongs in in the original file.

## Reconstructor

To reconstruct a file, run `sh reassemble_chunks.sh $commonName $numChunks`, where `$commonName` is the name shared by all the chunk files (i.e., the name before the final underscore and `$chunkNumber`), and $numChunks is the greatest chunk number (inclusive). The output is the reconstituted file, named `$commonName`_assembled 

# Example

Suppose I have a 105 megabyte file named `LargeFile.txt`. Running `python split_file_chunks.py LargeFile.txt 25` will create 5 chunk files, `LargeFile.txt_0`, `LargeFile.txt_1`, `LargeFile.txt_2`, `LargeFile.txt_3`, and `LargeFile.txt_4`. Chunk files 0-3 will be 25 megabytes, but chunk file 4 will only be 5 megabytes, because that is all thats left in `LargeFile.txt` by the time we get to that round of splitting. To reassemble the chunks, I run `sh reassemble_chunks.sh LargeFile.txt 4`, which will `cat` the contents of the chunk files into a new file called `LargeFile.txt_assembled`. Once finished, `LargeFile.txt_assembled` and `LargeFile.txt` will be the exact same.To verify this, you can take and compare their hashes using a cryptographic hash function (md5, sha1, sha256, etc).

# Bugs/Troubleshooting

I build this pair of programs with a specific purpose in mind, so it is likely that not all possible cases are handled correctly. If you encounter a bug with this project, feel free to create a pull request or raise an issue. I'll try and respond ASAP. 

