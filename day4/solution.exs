defmodule Solution do
  def is({x, y}, pattern, text, map, allow_reverse \\ false) do
    size = map |> Kernel.map_size() |> :math.sqrt() |> trunc()

    mapped_pts =
      for {dx, dy} <- pattern,
          (x + dx) in 0..size,
          (y + dy) in 0..size,
          do: {x + dx, y + dy}

    found =
      for {x, y} <- mapped_pts,
          into: "",
          do: Map.get(map, {x, y}, "")

    text == found or (allow_reverse and text == String.reverse(found))
  end
end

lines =
  File.read!("input.txt")
  |> String.split("\n")

map =
  for {line, y} <- Enum.with_index(lines),
      {char, x} <- Enum.with_index(String.graphemes(line)),
      into: %{},
      do: {{x, y}, char}

patterns1 = [
  [{0, 0}, {1, 1}, {2, 2}, {3, 3}],
  [{0, 0}, {0, 1}, {0, 2}, {0, 3}],
  [{0, 0}, {-1, 1}, {-2, 2}, {-3, 3}],
  [{0, 0}, {-1, 0}, {-2, 0}, {-3, 0}],
  [{0, 0}, {-1, -1}, {-2, -2}, {-3, -3}],
  [{0, 0}, {0, -1}, {0, -2}, {0, -3}],
  [{0, 0}, {1, -1}, {2, -2}, {3, -3}],
  [{0, 0}, {1, 0}, {2, 0}, {3, 0}]
]

patterns2 = [
  [{-1, -1}, {0, 0}, {1, 1}],
  [{1, -1}, {0, 0}, {-1, 1}]
]

map
|> Enum.filter(fn {_, val} -> val == "X" end)
|> Enum.map(fn {{x, y}, _} ->
  Enum.count(patterns1, &Solution.is({x, y}, &1, "XMAS", map, false))
end)
|> Enum.sum()
|> IO.inspect(label: "p1")

map
|> Enum.filter(fn {_, val} -> val == "A" end)
|> Enum.map(fn {{x, y}, _} ->
  (Enum.all?(patterns2, &Solution.is({x, y}, &1, "MAS", map, true)) && 1) || 0
end)
|> Enum.sum()
|> IO.inspect(label: "p2")
