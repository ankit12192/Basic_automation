from testcases import*

def run_cases():
    objj = user()
    objj.case_list_user(2)
    objj.case_create_user(name="Ankit", job="QA")
    objj.case_blank_name()
    objj.case_blank_job()
    objj.case_update_user(100, "ANk", "sa")
    objj.update_case_blank_name(2)
    objj.update_blank_job(2)
    objj.delete_user(2)
