import requests 
from bs4 import BeautifulSoup

def search_incriut():
    keyword = "파이썬"
    url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0" 
    # 주소에서 "?"까지가 파일명 그 뒤엔 파라미터임. 깨진 부분에 keyword 넣기

    response = requests.get(url)

    # 출력이 200 또는 200번대이면 요청 성공, 400 또는 400번대이면 오류
    # print(response.status_code)
    # print(response)
    # print(response.content)

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify)

    lis = soup.find_all("li", class_="c_col")
    # print(lis)
    # print(len(lis))

    jobs = []

    for li in lis:
        company = li.find("a", class_ = "cpname").text
        # print(company)
    
        title = li.find("div", class_="cell_mid").find("a").text
        # print(title)
        
        href = li.find("div", class_="cell_mid").find("a").get("href")
        # print(href)
        
        location = li.find("div", class_ = "cl_md").find_all("span")[0].text
        # print(location)

        job_data = {
        "title": title,
        "company": company,
        "location": location,
        "herf": href    
        }

        jobs.append(job_data)

    # print(jobs)
    return jobs
