module CollatzPlot
include("collatz.jl")
using PyPlot
# using Winston

  function collatz_plot(n)
    number, chain_length, chain = Collatz.longest_chain(n)

    x::Array{Int64} = [2:n-1]
    y = Int64[]
    for i in x
      push!(y, chain[i])
    end
    plot(x, y, color = "red", linewidth = 1.5, linestyle = "-")
    ylabel("Chain Length")
    xlabel("Natural Number")
    title("Plot of Natural Number vs Collatz Chain Length")

  end

end
