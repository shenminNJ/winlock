# A sample Guardfile
# More info at https://github.com/guard/guard#readme

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard 'shell' do
  watch(/.*/) do |m|
    "#{m} has changed."
    `rsync -vr --checksum ./ rsync://155.98.92.158/projects/winlock/`
    `echo "NO OP" | nc 155.98.92.158 880`
  end
end
