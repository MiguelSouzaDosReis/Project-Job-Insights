from src.jobs import read


def get_unique_job_types(path):
    readThePath = read(path)

    filtered_readThePath = [
        filtered_job_type["job_type"] for filtered_job_type in readThePath
    ]
    unique_job_types = list(set(filtered_readThePath))
    # print(unique_job_types)
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_readThePath = [
        filter_job_in_job_types
        for filter_job_in_job_types in jobs
        if filter_job_in_job_types["job_type"] == job_type
    ]
    # print(filtered_readThePath)
    return filtered_readThePath


def get_unique_industries(path):
    readThePath = read(path)

    filtered_readThePath = [
        filtered_industry["industry"]
        for filtered_industry in readThePath
        if filtered_industry["industry"] != ""
    ]
    unique_industry = set(filtered_readThePath)
    # print(unique_industry)
    return unique_industry


def filter_by_industry(jobs, industry):
    filtered_readThePath = [
        filter_job_in_industry
        for filter_job_in_industry in jobs
        if filter_job_in_industry["industry"] == industry
    ]
    # print(filtered_readThePath)
    return filtered_readThePath


def get_max_salary(path):
    readThePath = read(path)

    filtered_readThePath = [
        int(filtered_max_salary["max_salary"])
        for filtered_max_salary in readThePath
        if filtered_max_salary["max_salary"].isnumeric()
    ]
    unique_max_salary = filtered_readThePath
    bigger = unique_max_salary[0]
    for number in unique_max_salary:
        if number > bigger:
            bigger = number
    # print(bigger)
    return bigger


def get_min_salary(path):
    readThePath = read(path)

    filtered_readThePath = [
        int(filtered_min_salary["min_salary"])
        for filtered_min_salary in readThePath
        if filtered_min_salary["min_salary"].isnumeric()
    ]
    unique_min_salary = list(filtered_readThePath)
    smaller = unique_min_salary[0]
    for number in unique_min_salary:
        if number < smaller:
            smaller = number
    # print(smaller)
    return smaller


def matches_salary_range(job, salary):
    try:
        if job.get("min_salary") is None or job.get("max_salary") is None:
            raise ValueError
        elif job["min_salary"] > job["max_salary"]:
            raise ValueError
        int(job["min_salary"]) and int(job["max_salary"])
        int(salary)
    except (ValueError, TypeError):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_readThePath = []
    for filter_job in jobs:
        try:
            if matches_salary_range(filter_job, salary):
                filtered_readThePath.append(filter_job)
        except ValueError:
            pass
    # print(filtered_readThePath)
    return filtered_readThePath
