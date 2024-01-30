#!/usr/bin/env ruby
str=""
str += ARGV[0].scan(/\[from:(.*?)\]/).join
str += (',')
str += ARGV[0].scan(/\[to:(.*?)\]/).join
str += (',')
str += ARGV[0].scan(/\[flags:(.*?)\]/).join
puts str
