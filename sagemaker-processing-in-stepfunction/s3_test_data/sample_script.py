if __name__ == "__main__":
    with open('/opt/ml/processing/input/data.txt', 'r') as f:
        name = f.read()

        with open('/opt/ml/processing/output/output.txt', 'w') as f:
            f.write(f'Hello, {name}!')
