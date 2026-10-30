#!/usr/bin/env ruby
<<<<<<< HEAD
puts ARGV[0].scan(/from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")
=======
Format = ARGV[0].scan(/from:(.\w+)|to:(.\w+)|flags:([0-9:-]+)/)
List = [Format[0].compact, Format[1].compact, Format[2].compact]
puts List.join(',')
>>>>>>> 1344d66a427a81fc111b5d4cbef668446ed7e34c
