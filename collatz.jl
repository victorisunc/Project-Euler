module Collatz
# PROJECT EULER
# PROBLEM 14:

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 10 terms.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.

# Which starting number, under one million, produces the largest chain?

  function longest_chain(n)
    longest_chain_yet::Int64 = 0
    counter::Int64 = 0
    number_chain_length = Dict{Int64, Int64}()
    temp_sequence_length::Int64 = 0
    largest_starting_number::Int64 = 0

    for i in 1:n-1
      number = i
      counter += 1
      while number != 1
        if haskey(number_chain_length, number)
          temp_sequence_length = number_chain_length[number] - 1
          break
        end

        if iseven(number)
          number = div(number, 2)
        else
          number = 3 * number + 1
        end
        counter += 1
      end
      current_chain_length = number_chain_length[i] = counter + temp_sequence_length
      temp_sequence_length = 0

      if longest_chain_yet < current_chain_length
        longest_chain_yet = current_chain_length
        largest_starting_number = i
      end
      counter = 0
    end
    println("Under $n,")
    println("the largest starting number is: $largest_starting_number")
    println("with longest chain of: $(number_chain_length[largest_starting_number])")
    (largest_starting_number, number_chain_length[largest_starting_number], number_chain_length)
  end

end