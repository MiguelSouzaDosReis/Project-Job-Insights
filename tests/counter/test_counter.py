from src.counter import count_ocurrences


def test_counter():
    jobs = "src/jobs.csv"
    assert count_ocurrences(jobs, "python") == count_ocurrences(jobs, "PYTHON")
