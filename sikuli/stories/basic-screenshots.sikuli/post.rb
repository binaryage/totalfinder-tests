#!/usr/bin/env ruby

require 'rubygems'
begin
  require 'rmagick'
  include Magick
rescue LoadError
  raise 'You must "sudo gem install rmagick"'
end

##########################################################################################

ROOT_DIR = File.expand_path(File.dirname(__FILE__))
PRODUCTS_DIR = File.expand_path(File.join(ROOT_DIR, "..", "..", "..", "products"))
SCREENS_DIR = File.expand_path(File.join(PRODUCTS_DIR, "screens"))

##########################################################################################

class Dir
    def self.list( options = {} )
        options = { :directory => Dir.pwd(), :pattern => '*.*', :order => 'ASC' }.merge options
        files = glob( File.join(options[:directory], options[:pattern]) ).sort_by do |file|
            File.mtime(file)
        end
        files.reverse! if options[:order] == 'DESC'
        files
    end
end

##########################################################################################

def copy_screenshot(file,  name)
    dest = File.join(SCREENS_DIR, name)
    `cp "#{file}" "#{dest}"`
end

def compose_screenshot(file1, file2, name)
    image1 = ImageList.new(file1)
    image2 = ImageList.new(file2)
    result = image1.composite(image2, Magick::SouthGravity, 0, 55, Magick::OverCompositeOp)
    result.write(File.join(SCREENS_DIR, name))
end

def compose_dual_screenshot(chrome, left, right, name)
    image1 = ImageList.new(chrome)
    image2 = ImageList.new(left)
    image3 = ImageList.new(right)
    result = image1.composite(image2, Magick::SouthEastGravity, 40, 55, Magick::OverCompositeOp)
    result2 = result.composite(image3, Magick::SouthWestGravity, 40, 55, Magick::OverCompositeOp)
    result2.write(File.join(SCREENS_DIR, name))
end

##########################################################################################

grab_dir = `defaults read com.apple.screencapture location 2>&1`
grab_dir = File.expand_path("~/Desktop") if grab_dir =~ /does not exist/

list = Dir.list({:directory => grab_dir, :pattern => "*.png", :order => 'DESC'})

list = list[0..15].reverse
puts list

compose_screenshot(list[0], list[1], "tabs.png")
compose_dual_screenshot(list[2], list[3], list[4], "dual-mode.png")

copy_screenshot(list[5], "menu-finder.png")
copy_screenshot(list[6], "menu-file.png")
copy_screenshot(list[7], "menu-edit.png")
copy_screenshot(list[8], "menu-view.png")
copy_screenshot(list[9], "menu-go.png")
copy_screenshot(list[10], "menu-window.png")
copy_screenshot(list[11], "menu-help.png")

copy_screenshot(list[12], "pref-visor.png")
copy_screenshot(list[13], "pref-asepsis.png")
copy_screenshot(list[14], "pref-tweaks.png")
copy_screenshot(list[15], "pref-about.png")
