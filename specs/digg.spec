require './spec_helper'
require 'pagination_render_logic/digg'

# First Previous 1 2 3 ... 22 23 24 25 26 [27] 28 29 30 31 32 ... 48 49 50 Next Last

class DiggRenderer
  extend PaginationRenderLogic::Digg
end

class DiggObject
  include PaginationRenderLogic::Digg
end

describe DiggRenderer do
  
  before do
    DiggRenderer.config :total_pages => 10, :current_page => 1, 
                        :after_first_page => 3, :arround_current_page => 5
  end
  
  it "should be awesome" do
  end
  
  it "should set sections correctly" do
    # [1] 2 3 4 5 6 ... 8 9 10 Next Last
    DiggRenderer.total_pages = 10
    DiggRenderer.current_page = 1
    DiggRenderer.setup
    DiggRenderer.should have(6).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(3).last_page_section
    DiggRenderer.middle_section.should eql((1..6).to_a)
    DiggRenderer.last_page_section.should eql((8..10).to_a)
    
    # [1] 2 3 4 5 6 7 8 9 Next Last
    DiggRenderer.total_pages = 9
    DiggRenderer.current_page = 1
    DiggRenderer.setup
    DiggRenderer.should have(9).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..9).to_a)
    
    # 1 2 3 ... 5 6 7 8 9 [10] Next Last
    DiggRenderer.total_pages = 10
    DiggRenderer.current_page = 10
    DiggRenderer.setup
    DiggRenderer.should have(6).middle_section
    DiggRenderer.should have(3).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((5..10).to_a)
    DiggRenderer.first_page_section.should eql((1..3).to_a)
    
    # First Previous 1 2 3 ... 22 23 24 25 26 [27] 28 29 30 31 32 ... 48 49 50 Next Last
    DiggRenderer.total_pages = 50
    DiggRenderer.current_page = 27
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(3).first_page_section
    DiggRenderer.should have(3).last_page_section
    DiggRenderer.middle_section.should eql((22..32).to_a)
    DiggRenderer.first_page_section.should eql((1..3).to_a)
    DiggRenderer.last_page_section.should eql((48..50).to_a)
  end  
  
  it "should render links properly" do

    # [1] 2 3 Next Last
    DiggRenderer.total_pages = 3
    DiggRenderer.current_page = 1
    DiggRenderer.setup
    DiggRenderer.should have(3).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..3).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should_not have_first_page
    DiggRenderer.should_not have_previous_page
    
    # First Previous 1 [2] 3 Next Last
    DiggRenderer.total_pages = 3
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(3).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..3).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page

    # First Previous 1 2 [3]
    DiggRenderer.total_pages = 3
    DiggRenderer.current_page = 3
    DiggRenderer.setup
    DiggRenderer.should have(3).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..3).to_a)
    DiggRenderer.should_not have_next_page
    DiggRenderer.should_not have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 [2] 3 4 5 Next Last
    DiggRenderer.total_pages = 5
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(5).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..5).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page

    # First Previous 1 [2] 3 4 Next Last
    DiggRenderer.total_pages = 4
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(4).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..4).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
 
    # First Previous 1 [2] 3 4 5 6 7 8 9 Next Last
    DiggRenderer.total_pages = 9
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(9).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..9).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page

    # First Previous 1 [2] 3 4 5 6 7 8 9 10 Next Last
    DiggRenderer.total_pages = 10
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(10).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..10).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 [2] 3 4 5 6 7 ... 9 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 2
    DiggRenderer.setup
    DiggRenderer.should have(7).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(3).last_page_section
    DiggRenderer.last_page_section.should eql((9..11).to_a)
    DiggRenderer.middle_section.should eql((1..7).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # empty
    DiggRenderer.total_pages = 0
    DiggRenderer.current_page = 1
    DiggRenderer.setup
    DiggRenderer.should_not have_links
    
    # empty
    DiggRenderer.total_pages = 1
    DiggRenderer.current_page = 1
    DiggRenderer.setup
    DiggRenderer.should_not have_links
    
    # First Previous 1 2 [3] 4 5 6 7 8 9 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 3
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 4 5 [6] 7 8 9 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 6
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 4 5 6 [7] 8 9 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 7
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 4 5 6 7 [8] 9 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 8
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 4 5 6 7 8 [9] 10 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 9
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.should have(0).first_page_section
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((1..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 ... 5 6 7 8 9 [10] 11 Next Last
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 10
    DiggRenderer.setup
    DiggRenderer.should have(7).middle_section
    DiggRenderer.should have_first_page_section
    DiggRenderer.should_not have_last_page_section
    DiggRenderer.should have(3).first_page_section
    DiggRenderer.first_page_section.should eql((1..3).to_a)
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((5..11).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 ... 6 7 8 9 10 [11]
    DiggRenderer.total_pages = 11
    DiggRenderer.current_page = 11
    DiggRenderer.setup
    DiggRenderer.should have(6).middle_section
    DiggRenderer.should have_first_page_section
    DiggRenderer.should_not have_last_page_section
    DiggRenderer.should have(3).first_page_section
    DiggRenderer.first_page_section.should eql((1..3).to_a)
    DiggRenderer.should have(0).last_page_section
    DiggRenderer.middle_section.should eql((6..11).to_a)
    DiggRenderer.should_not have_next_page
    DiggRenderer.should_not have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
    
    # First Previous 1 2 3 ... 22 23 24 25 26 [27] 28 29 30 31 32 ... 48 49 50 Next Last
    DiggRenderer.total_pages = 50
    DiggRenderer.current_page = 27
    DiggRenderer.setup
    DiggRenderer.should have(11).middle_section
    DiggRenderer.middle_section.should eql((22..32).to_a)
    DiggRenderer.should have_first_page_section
    DiggRenderer.should have_last_page_section
    DiggRenderer.should have(3).first_page_section
    DiggRenderer.first_page_section.should eql((1..3).to_a)
    DiggRenderer.should have(3).last_page_section
    DiggRenderer.last_page_section.should eql((48..50).to_a)
    DiggRenderer.should have_next_page
    DiggRenderer.should have_last_page
    DiggRenderer.should have_first_page
    DiggRenderer.should have_previous_page
  end
  
end