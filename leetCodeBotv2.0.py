
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

crfToken = "XiUuuWRBxhoWjk3KXzx6HngPSB1vKdPTWyBYIyMMeGzqjFhiXpBycsLOJ1U6Or5Z"
cookies = {}
headers={
'Host':'leetcode.com',
'Cookie':'gr_user_id=b4d8df18-58c7-47e7-8dd2-a19521786561; __stripe_mid=a127044c-83b8-4521-ae20-107e6b66d34f5e97be; 87b5a3c3f1a55520_gr_last_sent_cs1=Evil-Beast; FCNEC=%5B%5B%22AKsRol_QJT8sMKH-JTyxwVsWWbM-Q2BrN36izMalZOG5bbHAMQrW7XYTy0T-jjkJ1NcpfpF51d-3gR4jIKLFtN8d-k6E6svaBd1RmxcU8sOKjzutCcuN8kAe-mtcaPOwFX4RwI9xR1CQsHWXemLMeztKK3EJTtKhZg%3D%3D%22%5D%5D; csrftoken=XiUuuWRBxhoWjk3KXzx6HngPSB1vKdPTWyBYIyMMeGzqjFhiXpBycsLOJ1U6Or5Z; __gads=ID=550f4215b1e21055:T=1706884903:RT=1707409781:S=ALNI_Mamk1dKWvcG4nIp1y8TdNGyKv5RYA; __gpi=UID=00000cf6fcdb25a6:T=1706884903:RT=1707409781:S=ALNI_MZt1BOgt9FHgBw5umkhDGNkM7x8fg; __eoi=ID=7e0da3b57e8cd91e:T=1706884903:RT=1707409781:S=AA-AfjYwdFs3Gi3766HKfZugkFyu; _ga=GA1.1.114086227.1706865609; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTE1NjE4NDAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiZjc3MWFhODc4ODUzMTQ2N2I2NjE4NTkyNjliY2VjYTI3NjRiNzY3ZDlkOTJlOTE0YjhmMzcxNzVjNjg2YWIyIiwiaWQiOjExNTYxODQwLCJlbWFpbCI6Im5hbmRha2lzaG9yZXAyMTJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJFdmlsLUJlYXN0IiwidXNlcl9zbHVnIjoiRXZpbC1CZWFzdCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNzAxMTQ3NjE5LnBuZyIsInJlZnJlc2hlZF9hdCI6MTcwNzY3MTUzNSwiaXAiOiIxNTcuNTEuODUuMyIsImlkZW50aXR5IjoiMDMzZjM1MTFjMzA5YzY3MmNjYjdmNTkzY2ZhNjYyZjIiLCJzZXNzaW9uX2lkIjo1NTIzNTI2Mn0._0EVjUnPJ13OeFXjmMKMR_m_rPV4o8HbBgztdnq1EQk; 87b5a3c3f1a55520_gr_session_id=5aa15de8-6c7c-41c3-ab97-7bf31b3ad076; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=5aa15de8-6c7c-41c3-ab97-7bf31b3ad076; 87b5a3c3f1a55520_gr_cs1=Evil-Beast; 87b5a3c3f1a55520_gr_session_id_sent_vst=5aa15de8-6c7c-41c3-ab97-7bf31b3ad076; _ga_CDRWKZTDEX=GS1.1.1707671535.15.0.1707671570.25.0.0',
'Sec-Ch-Ua':'"Chromium";v="121","NotA(Brand";v="99"',
'Content-Type':'application/json',
'Sec-Ch-Ua-Mobile':'?0',
'X-Csrftoken': crfToken,
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36',
'Sec-Ch-Ua-Platform':'"Windows"',
'Accept':'*/*',
'Origin':'https://leetcode.com',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://leetcode.com/',
'Accept-Encoding':'gzip,deflate, utf-8',
'Accept-Language':'en-US,en;q=0.9',
'Priority':'u=1,i',
}
problemsData = {"query":"\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ","variables":{"categorySlug":"all-code-essentials","skip":2000,"limit":1000,"filters":{}},"operationName":"problemsetQuestionList"}
problems = requests.post(url="https://leetcode.com/graphql/",headers=headers,json=problemsData).json()
problems = problems['data']['problemsetQuestionList']['questions'] #problems[i]['titleSlug']
pcount = 128
totalQuestionDone = 0
options = Options()
options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-image-loading')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))
webTags = ['     	  ','\t','    ','     ','\n','<li>','</li>','</sup>','<sup>','&nbsp;','</font>','<font face="monospace">','<p>','</p>','<code>','</code>','<em>','</em>','<strong>','</strong>','<pre>','</pre>','<strong class="example">','<ul>','</ul>']
def cleanCode(badcode):
    goodcode = ''
    for i in badcode:
        isit = True
        for j in i:
            if isit:
                if j.isnumeric():
                    continue
                else:
                    isit = False
                    goodcode += j
            else:
                goodcode += j
        goodcode += "\n"
    return goodcode

def buttons(browser,xpath):
    time.sleep(3)
    browser.find_element('xpath',xpath).submit()
    time.sleep(3)

def inputtxt(browser,value,xpath):
    time.sleep(3)
    field = browser.find_element('xpath', xpath)
    field.clear()
    field.send_keys(value)

def getcode(coder):
  time.sleep(3)
  return coder.find_element(By.CSS_SELECTOR, "body > div.flex.flex-col.min-h-screen > main > div > div.group.w-full.overflow-auto.pl-0.animate-in.duration-300.ease-in-out.peer-\[\[data-state\=open\]\]\:lg\:pl-\[250px\].peer-\[\[data-state\=open\]\]\:xl\:pl-\[300px\] > div.pb-\[110px\].pt-4 > div > div:nth-child(2) > div.group.relative.mb-4.flex.items-start.md\:-ml-12 > div.ml-4.flex-1.space-y-2.overflow-hidden.px-1 > div.prose.break-words.dark\:prose-invert.prose-p\:leading-relaxed.prose-pre\:p-0 > pre > div > div:nth-child(2) > code").text

def Connecting_To_Browser(coder):
    global totalQuestionDone
    currentProblemSlug = problems[pcount]['titleSlug']
    print(currentProblemSlug)
    getProblemData = {
        "query": "\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n    dataSchemas\n  }\n}\n    ",
        "variables": {"titleSlug": f"{currentProblemSlug}"}, "operationName": "questionContent"}
    problemDesc = requests.post('https://leetcode.com/graphql/',headers=headers,json=getProblemData).json()['data']['question']['content']
    pd = ""
    for i in webTags:
        problemDesc = problemDesc.replace(i," ")
    for i in problemDesc.split(" "):
        if i=="Constraints:":
            break
        pd+=i
        pd+=" "
    problemDesc = pd

    time.sleep(1)

    getInputData = {
        "query": "\n    query consolePanelConfig($titleSlug: String!) {\n  question(titleSlug: $    titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    enableDebugger\n    enableRunCode\n    enableSubmit\n    enableTestMode\n    exampleTestcaseList\n    metaData\n  }\n}\n    ",
        "variables": {"titleSlug": f"{currentProblemSlug}"}, "operationName": "consolePanelConfig"}
    
    
    inputData = requests.post('https://leetcode.com/graphql/', headers=headers, json=getInputData).json()['data']['question']
    currentProblemId = inputData['questionId']
    inputData = inputData['exampleTestcaseList']
    
    dataInput = ""
    for i in inputData:
        dataInput+=str(i)
        dataInput+="\n"
    dataInput = dataInput[:-1]
    time.sleep(1)

    getStarting = {"query":"\n    query questionEditorData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      code\n    }\n    envInfo\n    enableRunCode\n    hasFrontendPreview\n    frontendPreviews\n  }\n}\n    ","variables":{"titleSlug":f"{currentProblemSlug}"},"operationName":"questionEditorData"}
    starting = requests.post('https://leetcode.com/graphql/', headers=headers, json=getStarting).json()['data']['question']['codeSnippets'][3]['code']
    print("Got code Frags ")
    starting = starting.replace('\n',' ')
    starting = starting.split("\n")
    for i in starting:
        if "#" in i:
            starting.remove(i)
    fll = ""
    for i in starting:
        fll += i
    starting = fll
    time.sleep(1)
    coder.get("https://blackbox.ai/")
    time.sleep(10)
    botInput = f"give me a single python3 code with less time complexisity for a question without comments and without usage and only one member fuction.The program should start like '{starting}' and the question is {problemDesc}"
    inputtxt(coder,botInput,'//*[@id="chat-input-box"]')
    buttons(coder,'//*[@id="send-button"]')
    time.sleep(30)
    badcode = getcode(coder)
    badcode = badcode.split('\n')
    goodcode = cleanCode(badcode)
    print("\n")
    print(goodcode)
    print("\n")
    time.sleep(1)
    runCodeData = {"lang":"python3","question_id":currentProblemId,"typed_code":goodcode,"data_input":dataInput}
    runcode = requests.post(f'https://leetcode.com/problems/{currentProblemSlug}/interpret_solution/',headers=headers,json=runCodeData)
    print("\n")
    print(runcode.content)
    print("\n")
    runcode = runcode.json()
    time.sleep(1)
    while True:
        checkRanCode = requests.post(f'https://leetcode.com/submissions/detail/{runcode["interpret_id"]}/check/',headers=headers).json()
        print("Running Code")
        if(checkRanCode['state']=="SUCCESS"):
            if checkRanCode['status_msg'] != 'Accepted':
                print(checkRanCode)
                return
            else:
                break
        else:
            time.sleep(3)
    submitCodeData = {"lang":"python3","question_id":currentProblemId,"typed_code": goodcode}
    submitCode = requests.post('https://leetcode.com/problems/two-sum/submit/',headers=headers,json=submitCodeData).json()

    while True:
        checkSubmitCode = requests.post(f'https://leetcode.com/submissions/detail/{submitCode["submission_id"]}/check/',headers=headers).json()
        print("Submitting Code")
        if(checkSubmitCode['state']=="SUCCESS"):
            if checkSubmitCode['status_msg'] != 'Accepted':
                print(checkSubmitCode)
                print("\n-------Submission Failed--------\n")
                return
            else:
                totalQuestionDone +=1
                f = open("pcount.txt", "w")
                f.write(f"Last Question pcount {pcount}")
                f.close()
                print("\n\n\n-------------------Submission Success-----------------\n")
                print(f"-----------------Total Questions {totalQuestionDone}----------------")
                print(f"\n--------------------Last Question Id {currentProblemId}----------------\n\n\n")
                break
        else:
            time.sleep(3)

def call_funct():
    global pcount
    while True:
        coder = webdriver.Chrome(options=options)
        try:
            Connecting_To_Browser(coder)
            pcount += 1
            time.sleep(15)
            coder.quit()
        except Exception as e:
            coder.quit()
            print(e)
            tb = e.__traceback__
            pcount += 1
            time.sleep(10)


print("Started")
call_funct()
# coder = webdriver.Chrome(options=options)
# Connecting_To_Browser(coder)



