import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    options = PipelineOptions(runner="DirectRunner")

    with beam.Pipeline(options=options) as p:

        word_counts = (
            p
            | "Read Input" >> beam.io.ReadFromText("input.txt")
            | "Split Words" >> beam.FlatMap(lambda line: line.split())
            | "To Lowercase" >> beam.Map(lambda word: word.lower())
            | "Map to Pair" >> beam.Map(lambda word: (word, 1))
            | "Count Words" >> beam.CombinePerKey(sum)
        )

        word_counts | "Print Output" >> beam.Map(lambda kv: print(f"{kv[0]} -> {kv[1]}"))


if __name__ == "__main__":
    run()
