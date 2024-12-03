defmodule Solution do
  def parse(text) do
    Regex.scan(~r/(mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\))/i, text)
    |> Enum.map(&Enum.uniq/1)
    |> Enum.map(&hd/1)
    |> Enum.map(fn instr ->
      [op | args] = String.split(instr, ~r/[\(\),]/, trim: true)
      [op | Enum.map(args, &String.to_integer/1)]
    end)
  end

  def part1(instructions) do
    instructions
    |> Enum.filter(&match?(["mul" | _], &1))
    |> Enum.map(fn [_, a, b] -> a * b end)
    |> Enum.sum()
  end

  def part2(instructions) do
    instructions
    |> Enum.reduce({0, true}, &process_instruction/2)
    |> elem(0)
  end

  defp process_instruction(["mul", a, b], {tot, true}), do: {a * b + tot, true}
  defp process_instruction(["do" | _], {tot, _}), do: {tot, true}
  defp process_instruction(["don't" | _], {tot, _}), do: {tot, false}
  defp process_instruction(_, acc), do: acc
end

text = File.read!("./input.txt")

Solution.parse(text)
|> Solution.part1()
|> IO.inspect()

Solution.parse(text)
|> Solution.part2()
|> IO.inspect()
