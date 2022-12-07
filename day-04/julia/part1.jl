

function solve()
    overlap_count = 0
    for line in eachline(stdin)
        a, b, c, d = parse.(Int, split(line, [',', '-']))
        range_x, range_y = a:b, c:d
        range_x, range_y = length(range_y) <= length(range_x) ? (range_x, range_y) : (range_y, range_x)
        overlap_count += issubset(range_y, range_x)
    end
    println(overlap_count)
end

solve()
