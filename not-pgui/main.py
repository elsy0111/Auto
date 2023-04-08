from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from time import sleep

driver_path = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_service = fs.Service(executable_path=driver_path)
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.implicitly_wait(2)

#? SET PROBLEM NUMBER =========================================


# CURRENT URL
print(driver.current_url)

for k in range(93,100):
    xpath = '//*[@id="nan-contents"]/div[7]/div/table/tbody/tr[' + str(k * 2 + (k+4)//5) + ']/td[1]/a'


# //*[@id="nan-contents"]/div[7]/div/table/tbody/tr[14]/td[1]/a

    select_drill = driver.find_element(By.XPATH,xpath)
    select_drill.click()

    #? ============================================================


    #? read_database =============================================

    filename = r'words_3gr\only\UNIT' + str(k).zfill(3) + '.txt'
    f = open(filename, 'r',encoding='UTF-8')
    data = list(f.read().replace(","," ").split())
    data_dict = {}

    for i in range(len(data)//2):
        data_dict[data[2 * i]] = data[2 * i + 1]

    def inverse_dict(d):
        return {v:k for k,v in d.items()}

    data_inverse_dict = inverse_dict(data_dict)

    #? ===========================================================

    sleep(.2)
    # SWITCH TO NEW TAB
    try:
        driver.switch_to.window(driver.window_handles[1])
    except:
        None

    # START
    # //*[@id="nan-contents-cover-buttons"]/div/div[1]/button/span[1]
    xpath = '//*[@id="nan-contents-cover-buttons"]/div/div[1]/button/span[1]'
    start_drill = driver.find_element(By.XPATH,xpath)
    start_drill.click()

    # Continue from the step you didn't complete?
    xpath = '/html/body/div[12]/div[3]/div/button[2]'
    try:
        no_restert = driver.find_element(By.XPATH,xpath)
        no_restert.click()
        ok_xpath = '/html/body/div[12]/div[3]/div/button/span'
        is_filled_xpath = '//*[@id="ui-id-6"]/div[3]/div/ul/li[20]'
    except:
        ok_xpath = '/html/body/div[13]/div[3]/div/button/span'
        is_filled_xpath = '//*[@id="ui-id-5"]/div[3]/div/ul/li[20]'

        pass

    #! DRILL1 ====================================================

    # Expraining
    sleep(1.5)
    ok_button = driver.find_element(By.XPATH,ok_xpath)
    ok_button.click()


    xpath = '//*[@id="nan-endless-inline"]/span'
    choice_left_path  = '//*[@id="nan-choice-0"]/span'
    choice_right_path = '//*[@id="nan-choice-1"]/span'

    xpath_res = '//*[@id="nan-endless-answer-column"]'
    xpath_process = '//*[@id="nan-endless-progress"]/div'

    print()
    while True:
        res = driver.find_element(By.XPATH,xpath_res)
        res_class = res.get_attribute("class")

        if res_class != "":
            continue

        process = driver.find_element(By.XPATH,xpath_process)
        process_style = process.get_attribute("style")

        ques_form = driver.find_element(By.XPATH,xpath)
        ques_text = ques_form.text
        
        try:
            ans_text = data_dict[ques_text]
        except:
            try:
                ans_text = data_inverse_dict[ques_text]
            except:
                break
        
        process_percent = int(process_style[-4:-2]) + 5

        print("process [","=" * 2 * int(process_percent/5) ,
            ">"," " *(40 - 2 * int(process_percent/5)),"] ",
            process_percent,"%",sep = "")

        print("prob   ",ques_text)
        print("ans    ",ans_text)
        print()

        choice_left  = driver.find_element(By.XPATH,choice_left_path)
        choice_right = driver.find_element(By.XPATH,choice_right_path)

        try:
            if choice_left.text == ans_text:
                ans_submit = choice_left
            else:
                ans_submit = choice_right

            ans_submit.click()
        except:
            continue

    # Next_step
    xpath = '//*[@id="nan-toolbox-footer"]/button/span[1]'
    next_step = driver.find_element(By.XPATH,xpath)
    next_step.click()

    #! ===========================================================

    #! DRILL2 ====================================================

    #expraining
    sleep(1)
    ok_button = driver.find_element(By.XPATH,ok_xpath)
    ok_button.click()


    q_xpath = '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]'

    print()
    process_percent = 0
    while True:
        #get_answer_text
        ques_form = driver.find_element(By.XPATH,q_xpath)
        ques_text = ques_form.text

        try:
            ans_text = data_dict[ques_text]
        except:
            ans_text = data_inverse_dict[ques_text]


        process_percent += 5

        print("process [","=" * 2 * int(process_percent/5) ,
            ">"," " *(40 - 2 * int(process_percent/5)),"] ",
            process_percent,"%",sep = "")
        print("prob   ",ques_text)
        print("ans    ",ans_text)
        print()

        #send_answer_text
        xpath = '//*[@id="nan-contents-qa-ex-center"]/div/div/div[5]/textarea'
        answer_input = driver.find_element(By.XPATH,xpath)
        answer_input.send_keys(ans_text + "\n")

        is_filled = driver.find_element(By.XPATH,is_filled_xpath)

        if is_filled.get_attribute("class") == "nan-pagination-sees":
            xpath = '//*[@id="nan-toolbox-footer"]/button/span[1]'
            next_step = driver.find_element(By.XPATH,xpath)
            next_step.click()
            break

        #next
        xpath = '//*[@id="nan-toolbox-content"]/div[2]/div[1]/button[2]/span[1]'
        next_ = driver.find_element(By.XPATH,xpath)
        next_.click()


    #! ===========================================================

    #! DRILL3 ====================================================

    #expraining
    sleep(.2)
    ok_button = driver.find_element(By.XPATH,ok_xpath)
    ok_button.click()

    xpath = '//*[@id="nan-toolbox-content"]/div[2]/div[1]/button[2]/span'
    sleep(.5)
    answer_button = driver.find_element(By.XPATH,xpath)
    answer_button.click()

    #next step
    xpath = '//*[@id="nan-toolbox-footer"]/button/span[1]'
    sleep(.5)
    next_step = driver.find_element(By.XPATH,xpath)
    next_step.click()


    #! ===========================================================

    #! DRILL4 ====================================================

    #expraining
    ok_button = driver.find_element(By.XPATH,ok_xpath)
    ok_button.click()

    xpath = '//*[@id="nan-vocabulary-inline"]/span'
    choice_left_path  = '/html/body/div[4]/div[2]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div[2]/button[1]/span'
    choice_right_path = '/html/body/div[4]/div[2]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div[2]/button[2]/span'


    xpath_process = '//*[@id="nan-vocabulary-progress"]/div'
    xpath_res = '//*[@id="nan-vocabulary-answer-overlay"]'

    while True:
        res = driver.find_element(By.XPATH,xpath_res)
        res_class = res.get_attribute("class")

        if res_class != "nan-invisible":
            continue

        process = driver.find_element(By.XPATH,xpath_process)
        process_style = process.get_attribute("style")

        ques_form = driver.find_element(By.XPATH,xpath)
        ques_text = ques_form.text

        try:
            ans_text = data_dict[ques_text]
        except:
            try:
                ans_text = data_inverse_dict[ques_text]
            except:
                break

        process_percent = int(process_style[-4:-2]) + 7

        print("process [","=" * 2 * int(process_percent/5) ,
            ">"," " *(40 - 2 * int(process_percent/5)),"] ",
            process_percent,"%",sep = "")

        print("prob   ",ques_text)
        print("ans    ",ans_text)
        print()

        choice_left  = driver.find_element(By.XPATH,choice_left_path)
        choice_right = driver.find_element(By.XPATH,choice_right_path)

        try:
            if choice_left.text == ans_text:
                ans_submit = choice_left
            else:
                ans_submit = choice_right
            ans_submit.click()
        except:
            continue

    # GOAL
    xpath = '//*[@id="nan-toolbox-footer"]/button/span[1]'
    goal_button = driver.find_element(By.XPATH,xpath)
    goal_button.click()

    # FINISH??
    yes_button = driver.find_element(By.XPATH,ok_xpath)
    yes_button.click()

    sleep(3)

    # SWITCH TO NEW TAB
    driver.switch_to.window(driver.window_handles[0])
    #! ===========================================================
