import numpy as np

def main():
    np.random.seed(853)

    mu, sigma = 0, 1
    sample_sizes = [10, 100, 1000, 10000]
    differences = []

    for size in sample_sizes:
        sample = np.random.normal(mu, sigma, size)
        sample_mean = np.mean(sample)
        diff = abs(mu - sample_mean)
        differences.append(diff)
        print(f"Sample size: {size}")
        print(f"  Difference between sample and population mean: {round(diff, 3)}")

    print("Follow first lecture")
    print("only 1 file change")
    print("modify hello.py")
    print(111)
if __name__ == "__main__":
    main()