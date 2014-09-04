function monty_sim(ngames)
  no_switch = 0
  switch = 0
  for game in 1:ngames
    player = rand(1:3)
    prize = rand(1:3)
    if player == prize
      no_switch += 1
    else
      switch += 1
    end
  end
  println("Probability of winning (own door): $(no_switch/ngames)")
  println("Probability of winning (switching door): $(switch/ngames)")
end

monty_sim(30000000)
