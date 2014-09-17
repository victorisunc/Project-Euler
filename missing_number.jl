module MissingNumber
  function gaussian_sum(n::Int64)
    div((n * (n + 1)), 2)
  end

  function find_unsorted(array_missing_a_number)
    array_length = length(array_missing_a_number)
    total_sum = gaussian_sum(array_length + 1)
    missing = total_sum - sum(array_missing_a_number)
    if missing == array_length + 1
      println("-1")
      return -1
    end
    println("find_unsorted, result: $missing")
    missing
  end

  function find_sorted_o_n(array_missing_a_number)
    for (index, value) in enumerate(array_missing_a_number)
      if index != value
        println("find_sorted_o_n, result: $index")
        return index
      end
    end
    println("find_sorted_o_n, result: -1")
    return -1
  end

  function find_sorted_o_log_n(array_missing_a_number)
    # sorted_list_missing_number = sort(array_missing_a_number)
    sorted_list_missing_number = array_missing_a_number
    len = length(array_missing_a_number)
    left = 0
    right = len - 1
    while left <= right
      middle = div((left + right), 2)
      if middle + 1 == sorted_list_missing_number[middle + 1]
        left = middle + 1
      else
        right = middle - 1
      end
    end
    if left + 1 > len
      println("find_sorted_o_log_n, result: -1")
      return -1
    else
      println("find_sorted_o_log_n, result: $(left + 1)")
      return left + 1
    end
  end
end