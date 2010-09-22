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

def crop_screenshot(list, name, x, y, w, h)
    file = list.shift
    image = ImageList.new(file)
    w = image.columns unless w
    h = image.rows unless h
    image.crop!(x, y, w, h)
    image.write(name)
end

def copy_screenshot(list,  name)
    file = list.shift
    `cp "#{file}" "#{name}"`
end

def compose_screenshot(list, name)
    file1 = list.shift
    file2 = list.shift
    image1 = ImageList.new(file1)
    image2 = ImageList.new(file2)
    result = image1.composite(image2, Magick::SouthGravity, 0, 55, Magick::OverCompositeOp)
    result.write(name)
end

def compose_dual_screenshot(list, name)
    chrome = list.shift
    left = list.shift
    right = list.shift
    image1 = ImageList.new(chrome)
    image2 = ImageList.new(left)
    image3 = ImageList.new(right)
    result = image1.composite(image2, Magick::SouthWestGravity, 40, 55, Magick::OverCompositeOp)
    result2 = result.composite(image3, Magick::SouthEastGravity, 40, 55, Magick::OverCompositeOp)
    result2.write(name)
end

##########################################################################################

grab_dir = `defaults read com.apple.screencapture location 2>&1`
grab_dir = File.expand_path("~/Desktop") if grab_dir =~ /does not exist/

list = Dir.list({:directory => grab_dir, :pattern => "*.png", :order => 'DESC'})

list = list[0..24].reverse
puts list

compose_screenshot(list, "tabs.png")
compose_dual_screenshot(list, "dual-mode.png")
compose_screenshot(list, "folders-on-top-enabled.png")
compose_screenshot(list, "folders-on-top-disabled.png")
compose_screenshot(list, "system-files-enabled.png")
compose_screenshot(list, "system-files-disabled.png")

crop_screenshot(list, "main-menu.png", 0, 0, 750, 0)

copy_screenshot(list, "menu-finder.png")
copy_screenshot(list, "menu-file.png")
copy_screenshot(list, "menu-edit.png")
copy_screenshot(list, "menu-view.png")
copy_screenshot(list, "menu-go.png")
copy_screenshot(list, "menu-window.png")
copy_screenshot(list, "menu-help.png")

copy_screenshot(list, "pref-visor.png")
copy_screenshot(list, "pref-asepsis.png")
copy_screenshot(list, "pref-tweaks.png")
copy_screenshot(list, "pref-about.png")