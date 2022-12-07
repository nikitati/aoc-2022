

function solve()
    overlap_count = 0
    for line in eachline(stdin)
        a, b, c, d = parse.(Int, split(line, [',', '-']))
        range_x, range_y = a:b, c:d
        overlap_count += !isempty(intersect(range_y, range_x))
    end
    println(overlap_count)
end

solve()
