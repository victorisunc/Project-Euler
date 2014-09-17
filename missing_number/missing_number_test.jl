using Base.Test

include("missing_number.jl")

custom_handler(r::Test.Success) = println("Success on $(r.expr)")
custom_handler(r::Test.Failure) = error("Error on custom handler: $(r.expr)")
custom_handler(r::Test.Error) = rethrow(r)

Test.with_handler(custom_handler) do
  # missing_number = 4
  # array_missing_a_number = [1,2,3,5]
  limit = 80000000
  missing_number = rand(1 : limit)
  array_missing_a_number = [1 : limit]
  splice!(array_missing_a_number, missing_number)

  missing = @time MissingNumber.find_unsorted(array_missing_a_number)
  @test missing == missing_number

  missing = @time MissingNumber.find_sorted_o_n(array_missing_a_number)
  @test missing == missing_number

  missing = @time MissingNumber.find_sorted_o_log_n(array_missing_a_number)
  @test missing == missing_number
end