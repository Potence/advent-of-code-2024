

def read_all(dir: str) -> list[list[int]]:
    """Read all reports from directory dir file and return all reports as
    a list of lists of integers

    Args:
        dir (str): file directory of file containing both lists

    Returns:
        list[list[int]]: list containing all reports
    """
    res = []
    
    with open(dir) as f:
        for line in f:    
            res.append([int(x) for x in line.split()])
    
    return res


def is_increasing(report: list[int]) -> bool:
    """Returns true if all levels in the report are increasing by 1,2, or 3
    otherwise returns False.

    Args:
        report (list[int]): contains all levels in the report

    Returns:
        bool: report is increasing
    """
    for i in range(1, len(report)):
        if not (1 <= report[i] - report[i - 1] <= 3):
            return False
    
    return True
    
    
def is_decreasing(report: list[int]) -> bool:
    """Returns true if all levels in the report are decreasing by 1,2, or 3
    otherwise returns False.

    Args:
        report (list[int]): contains all levels in the report

    Returns:
        bool: report is decreasing
    """
    for i in range(1, len(report)):
        if not (1 <= report[i - 1] - report[i] <= 3):
            return False
    
    return True
    
    
def main():
    reports_directory = r"D:\advent-of-code\day2\reports.txt"
    reports = read_all(reports_directory)
    res = [False] * len(reports)
    
    for i, report in enumerate(reports):
        res[i] = res[i] or is_increasing(report)
        res[i] = res[i] or is_decreasing(report)
    
    print(sum(res))


if __name__ == "__main__":
    main()
    