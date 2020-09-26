from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, datetime
import matplotlib.pyplot as plt
import numpy as np

asignaturas = ["rel", "quim", "fis", "dib", "len", "mat", "his", "ing", "tic"]
webs = [[""], ["https://classroom.google.com/u/2/c/MTU5NDU0MTI3MTY0", "http://www.gregthatcher.com/Chemistry/BalanceChemicalEquations.aspx", "https://ptable.com/?lang=es#Propiedades"], ["https://classroom.google.com/u/2/c/MTU5NzYxNTY0MjYy"], ["https://classroom.google.com/u/2/c/MTU5NjEzNjI3MTA3"], ["https://classroom.google.com/u/2/c/MTYzMzQ0OTEwOTQw"], ["https://classroom.google.com/u/2/c/MTYzMzY3MjkyODkz", "https://eljaria.jimdofree.com/"], ["https://classroom.google.com/u/2/c/MTU5NDQ4MTc3MDc2"], ["https://classroom.google.com/u/2/c/MTYyOTYxNjkzNTUy"], ["https://classroom.google.com/u/2/c/MTU5NjEzNjI3MDEy"]]
start_time = time.perf_counter()
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
plt.rcdefaults()
fig, ax = plt.subplots()
y_pos = np.arange(len(dias))

def end_session():
    file = open("save.txt","r")
    file_lines = file.readlines()
    file.close()
    file = open("save.txt", "w")
    total_secs = time.perf_counter() - start_time
    if datetime.datetime.today().weekday() == 0:
        file_lines = ["0\n", "0\n", "0\n", "0\n", "0\n", "0\n", "0\n"]
    file_lines[datetime.datetime.today().weekday()] = "{}\n".format(round(total_secs + int(file_lines[datetime.datetime.today().weekday()].replace("\n", ""))))
    file.writelines(file_lines)
    seconds = total_secs%60
    mins = total_secs/60 - (total_secs%60)/60
    hours = mins/60 - (mins%60)/60
    driver.quit()
    file.close()
    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i].replace("\n", "")
        file_lines[i] = int(file_lines[i])
    for i, v in enumerate(file_lines):
        ax.text(v + 3, i + .25, str(v), color='black')
    ax.barh(y_pos, file_lines, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dias)
    ax.invert_yaxis()
    ax.set_xlabel('Time')
    ax.set_title('Weekly study time')
    plt.show()
    print("That session lasted {}h {}m {}s".format(int(hours), int(mins), round(seconds)))
    sys.exit()

def buscar_asignatura():
    for i in range(len(asignaturas)):
        tasks = driver.find_elements_by_class_name("markdown_content")
        if tasks == []:
            tasks = driver.find_elements_by_class_name("task_content")
        if tasks == []:
            end_session()
        if asignaturas[i] in tasks[0].text:
            return asignaturas[i]

def open_tabs(class_name):
    for i in range(len(webs[asignaturas.index(class_name)])):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1+i])
        driver.get(webs[asignaturas.index(class_name)][i])
    driver.switch_to.window(driver.window_handles[0])

def check_update(tasks):
    last_pos = 0
    driver.switch_to.window(driver.window_handles[0])
    while True:
        tasks = driver.find_elements_by_class_name("markdown_content")
        if tasks == []:
            tasks = driver.find_elements_by_class_name("task_content")
        if tasks == []:
            end_session()
        pos = initial_tasks.index(tasks[0])
        if pos != last_pos:
            for i in range(len(driver.window_handles) - 1):
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
            open_tabs(buscar_asignatura())
        last_pos = pos
        tasks = driver.find_elements_by_class_name("markdown_content")
        if tasks == []:
            tasks = driver.find_elements_by_class_name("task_content")
        if tasks == []:
            end_session()
    time.sleep(5)


#Toodist boot
driver = webdriver.Firefox()
driver.get("https://todoist.com/users/showlogin")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="email"]').send_keys("nrivasm03@corazonistaslamina.com")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("20030326" + Keys.ENTER)
time.sleep(5)
tasks = driver.find_elements_by_class_name("markdown_content")
if tasks == []:
    tasks = driver.find_elements_by_class_name("task_content")
if tasks == []:
    end_session()
initial_tasks = tasks
clase = buscar_asignatura()

#open tabs depending on class
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(webs[asignaturas.index(clase)][0])
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("nrivasm03@corazonistaslamina.com" + Keys.ENTER)
time.sleep(3)
driver.find_element_by_class_name('whsOnd').send_keys("Crm1245n" + Keys.ENTER)
time.sleep(5)
for i in range(1, len(webs[asignaturas.index(clase)])):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1+i])
    driver.get(webs[asignaturas.index(clase)][i])
    time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
check_update(tasks)
