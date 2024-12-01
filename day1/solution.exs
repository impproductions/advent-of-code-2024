defmodule Solution do
  def part1(lines) do
    {left, right} = Enum.unzip(lines)

    Enum.zip(Enum.sort(left), Enum.sort(right))
    |> Enum.map(fn {l, r} -> abs(l - r) end)
    |> Enum.sum()
  end

  def part2(lines) do
    r_ref =
      lines
      |> Enum.map(fn {_l, r} -> r end)
      |> Enum.frequencies()

    lines
    |> Enum.map(fn {l, _r} -> l * (r_ref[l] || 0) end)
    |> Enum.sum()
  end
end

lines =
  File.stream!("./input.txt")
  |> Stream.map(&String.split(&1, [" ", "\n"], trim: true))
  |> Stream.map(fn [a, b] -> {String.to_integer(a), String.to_integer(b)} end)

IO.puts(Solution.part1(lines))
IO.puts(Solution.part2(lines))
