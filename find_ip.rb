#!/usr/bin/env ruby
# parses a txt to find IP using grep
# can use geolocation to locate the IPs
# and print them in a txt file

puts 'Enter location of txt'
txt_location = gets.chomp

# the grep command to find the IP, is broken down into four parts
# each part is the parses for the 3 digits of the IP
# can be narrowed down with specific values
command_1 = 'grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
command_2 = '\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
command_3 = '\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
command_4 = '\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"'

command = (command_1 + command_2 + command_3 + command_4)

# generates the IPs list array
ip_list = `#{command} #{txt_location}`.split

# prints the list with IPs
puts
puts ip_list
puts

# starts the geolocation
# uses the site ipinfo.io for the requests
print 'Use geolocation? y/n '
answer = gets.chomp

if answer == 'y' || answer == 'Y'

  time = Time.new
  time_now = time.strftime('%H.%M.%S')
  # creates a log file with a time stamp
  log = File.new('Desktop/ip_loc-' + time_now + '.log', 'w')

  ip_list.each do |i|
    location = `curl ipinfo.io/#{i}`
    puts location
    puts
    log.puts location
  end

  puts 'New log file created at ' + File.absolute_path(log)
end
