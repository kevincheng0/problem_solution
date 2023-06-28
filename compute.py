import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('threshold', type=float, help='Threshold that each input must meet')
    parser.add_argument('limit', type=float, help='Limit for the cumulative sum of all inputs')

    # Parse args
    args = parser.parse_args()
    threshold = args.threshold
    limit = args.limit

    # Read in variable number of lines
    line_count = 0
    lines = []
    while True:
        try:
            # Stop input if read an empty line
            line = input()
            if not line:
                break
        except EOFError:
            break

        lines.append(line)
        line_count += 1

    # Loop through lines to generate output
    to_print = []
    cumulative_value = 0
    for line in lines:
        try:
            # Mediate stdin inputs
            value = float(line)
        except ValueError as error:
            print(error)
            continue

        # Cap the output if the value modified by threshold will exceed limit
        modified_value = max(0, value - threshold)
        output_value = min(modified_value, limit - cumulative_value)

        cumulative_value += output_value
        to_print.append(output_value)

    to_print.append(cumulative_value)

    # Print all output
    for output in to_print:
        # Round to tenths precision for consistent values
        print(f'{output:.1f}')

if __name__ == '__main__':
    main()
