#import MontyHall
include("monty_hall.jl")

#@elapsed monty_sim(10000000)
#@time monty_sim(10000000)

no_switch, switch = @time MontyHall.monty_sim(1000000)

using Base.Test
@test_approx_eq_eps no_switch 0.333 0.01
@test_approx_eq_eps switch 0.667 0.01
