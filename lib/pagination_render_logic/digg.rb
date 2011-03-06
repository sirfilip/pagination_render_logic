module PaginationRenderLogic
  # Provides logic for building digg style pagination
  # First Previous 1 2 3 ... 22 23 24 25 26 [27] 28 29 30 31 32 ... 48 49 50 Next Last
  module Digg
    attr_accessor :total_pages, :current_page, 
                  :after_first_page, :arround_current_page, 
                  :middle_section, :first_page_section, :last_page_section
    
    def config(args = {})
      @total_pages = args[:total_pages] || 0
      @after_first_page = args[:after_first_page] || 3
      @arround_current_page = args[:arround_current_page] || 5
      @current_page = args[:current_page] || 1
    end
    
    def config!(args = {})
      config(args)
      setup
    end
  
    def setup
      @middle_section = ([current_page - arround_current_page, 1].max..[current_page + arround_current_page, total_pages].min).to_a
      @first_page_section = (1..[after_first_page, total_pages].min).to_a
      @last_page_section = ([1, total_pages - after_first_page + 1].max..total_pages).to_a
      if (total_pages / 2) > current_page
        merge_left
        merge_right
      else
        merge_right
        merge_left
      end
    end
    
    def has_next_page?
      @current_page < @total_pages
    end
    
    def next_page
      @current_page + 1
    end
    
    def has_last_page?
      @current_page < @total_pages
    end
    
    def last_page
      @total_pages
    end
    
    def has_first_page?
      @current_page > 1
    end
    
    def first_page
      1
    end
    
    def has_previous_page?
      @current_page > 1
    end
    
    def previous_page
      @current_page - 1
    end
    
    def has_links?
      @total_pages > 1
    end
    
    def has_first_page_section?
      not @first_page_section.empty?
    end
    
    def has_last_page_section?
      not @last_page_section.empty?
    end

private 
  
    def merge_left
      if (not @middle_section.empty?) and @middle_section.first - 1 <= @first_page_section.last
        @middle_section = @first_page_section | @middle_section
        @first_page_section.clear 
      end
    end
    
    def merge_right
      if (not @middle_section.empty?) and @middle_section.last + 1 >= @last_page_section.first
        @middle_section = @middle_section | @last_page_section
        @last_page_section.clear
      end
    end
    
  end
  
end