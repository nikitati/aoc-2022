#!/usr/bin/julia


function solve()
    calories = 0
    max_calories = 0
    for line in eachline(stdin)
        if line == ""
            max_calories = max(max_calories, calories)
            calories = 0
        else
            calories = calories + parse(Int, line)
        end
    end
    println(max_calories)
end

solve()
