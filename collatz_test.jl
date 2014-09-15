using Base.Test

include("collatz.jl")

custom_handler(r::Test.Success) = println("Success on $(r.expr)")
custom_handler(r::Test.Failure) = error("Error on custom handler: $(r.expr)")
custom_handler(r::Test.Error) = rethrow(r)

Test.with_handler(custom_handler) do
  number, chain_length = @time Collatz.longest_chain(5)
  @test number == 3
  # 3 10 5 16 8 4 2 1
  @test chain_length == 8

  number, chain_length = @time Collatz.longest_chain(8)
  @test number == 7
  # 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
  @test chain_length == 17

  number, chain_length = @time Collatz.longest_chain(7)
  @test number ==   6
  # 6 3 10 5 16 8 4 2 1
  @test chain_length == 9

  number, chain_length = @time Collatz.longest_chain(10)
  @test number == 9
  # 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
  @test chain_length == 20

  # Project Euler's Problem 14 Answer
  number, chain_length = @time Collatz.longest_chain(1000000)
  @test number == 837799
  @test chain_length == 525
end
