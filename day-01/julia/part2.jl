#!/usr/bin/julia

function accum_insert!(x::Int, accum::Vector{Int})
    min_idx = argmin(accum)
    if x > accum[min_idx]
        accum[min_idx] = x
    end
end

function solve()
    calories = 0
    accum = zeros(Int64, 3)
    for line in eachline(stdin)
        if line == ""
            accum_insert!(calories, accum)
            calories = 0
        else
            calories = calories + parse(Int, line)
        end
    end
    println(sum(accum))
end

solve()
