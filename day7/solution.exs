defmodule Solution do
  def can_eq([], res, _, tot), do: tot == res

  def can_eq([next | rest], res, ops, tot),
    do: Enum.any?(ops, fn op -> can_eq(rest, res, ops, op.(tot, next)) end)

  def cat(a, b), do: String.to_integer("#{a}#{b}")
end

eqs =
  File.read!("input.txt")
  |> String.split("\n")
  |> Enum.map(&String.split(&1, [": ", " "]))
  |> Enum.map(fn ls -> Enum.map(ls, &String.to_integer/1) end)
  |> Enum.map(fn [h | t] -> [h, t] end)

eqs
|> Enum.filter(fn [res, [next | rest]] -> Solution.can_eq(rest, res, [&+/2, &*/2], next) end)
|> Enum.map(&hd/1)
|> Enum.sum()
|> IO.inspect(label: "p1")

eqs
|> Enum.filter(fn [res, [next | rest]] ->
  Solution.can_eq(rest, res, [&+/2, &*/2, &Solution.cat/2], next)
end)
|> Enum.map(&hd/1)
|> Enum.sum()
|> IO.inspect(label: "p2")
