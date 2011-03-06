# -*- encoding: utf-8 -*-
$:.push File.expand_path("../lib", __FILE__)
require "pagination_render_logic/version"

Gem::Specification.new do |s|
  s.name        = "pagination_render_logic"
  s.version     = PaginationRenderLogic::VERSION
  s.platform    = Gem::Platform::RUBY
  s.authors     = ["sirfilip"]
  s.email       = ["github.sirfilip@gmail.com"]
  s.homepage    = "http://github.com/sirfilip/pagination_render_logic"
  s.summary     = %q{Will provide logic for rendering different types of pagination}
  s.description = %q{Will provide logic for rendering different types of pagination. ex floating digg style pagination}
  
  s.add_development_dependency("bundler")  
  s.add_development_dependency("rspec")

  s.licenses = ["MIT"]
  
  s.extra_rdoc_files = [
    "LICENSE.txt",
    "README.rdoc"
  ]

  s.rubyforge_project = "pagination_render_logic"

  s.files         = `git ls-files`.split("\n")
  s.test_files    = `git ls-files -- {test,spec,features}/*`.split("\n")
  s.executables   = `git ls-files -- bin/*`.split("\n").map{ |f| File.basename(f) }
  s.require_paths = ["lib"]
end
