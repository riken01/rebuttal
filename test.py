from openai import OpenAI
from collections import Counter
import re

client = OpenAI(
    api_key = ""
)

# from zhipuai import ZhipuAI
# client = ZhipuAI(api_key="eee04496e8a7fdacd2ee73ad80c6eab0.1KhlJX7j6tVAzvUm")
def get_number(input_string):
    # 使用正则表达式查找所有的小数
    numbers = re.findall(r"\d+\.\d+", input_string)
    # 取出前两个小数
    if len(numbers) < 2:
        return 0, 0
    positive, negative = float(numbers[0]), float(numbers[1])
    return positive, negative

def get_classfication_probabilities(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # engine = "deployment_name".
            n=10,
            messages=[
                # {"role": "system", "content": "Classify the topic of each news article in <<<NEWS>>> as 'World', 'Sports', 'Business', or 'Sci/Tech'. Give the topic classification without any other preamble text. \n ###EXAMPLE NEWS\nDollar Briefly Hits 4-Wk Low Vs Euro  LONDON (Reuters) - The dollar dipped to a four-week low  against the euro on Monday before rising slightly on  profit-taking, but steep oil prices and weak U.S. data  continued to fan worries about the health of the world's  largest economy.\nEXAMPLE OUTPUT\n Business"},
                {"role": "system", "content": "Classify the sentiment of each sentence in <<<SENTENCE>>> as'Positive' ,'Negative'. Give the sentiment classifications without any other preamble text. \n ###EXAMPLE SENTENCE\nHighly recommend this company for travel plans involving rail \nEXAMPLE OUTPUT\n Positive###"},
                {"role": "user", "content": "<<<" + text + ">>>"},
            ]
        )
        # response = client.chat.completions.create(
        #         model="glm-4-plus",  # 填写需要调用的模型编码
        #         messages=[
        #         {"role": "system", "content": "Classify the sentiment of each sentence in <<<SENTENCE>>> as'Positive' ,'Negative'. Give the sentiment classifications without any other preamble text. \n ###EXAMPLE SENTENCE\nHighly recommend this company for travel plans involving rail \nEXAMPLE OUTPUT\n Positive###"},
        #         {"role": "user", "content": "<<<" + text + ">>>"},
        #         ],
        #     )
        
        cnt_positive = 0
        cnt_negative = 0
        cnt_neutral = 0
        result_array = []
        for i in range(10):
            result = response.choices[i].message.content
            print(result)
            if "Positive" in result:
                result_array.append(1)
                # return 1
            elif "Negative" in result:
                # return 0
                result_array.append(0)

            # if "World" in result:
            #   result_array.append(0)
            # elif "Sports" in result:
            #   result_array.append(1)
            # elif "Business" in result:
            #   result_array.append(2)
            # elif "Sci/Tech" in result:
            #   result_array.append(3)
        

        count = Counter(result_array)
        most_common_num = count.most_common(1)[0][0]
        return most_common_num

        
    except Exception as e:
        print(f"error: {e},retry")
        return "error"
    
    # 读取 JSON 文件
import pandas as pd
data = pd.read_csv("RQ1/SST2/gpt2_medium.csv")

same_cnt = 0
cnt = 0
# 遍历每一条数据
for  line in data.itertuples():
    cnt += 1
    # if cnt >10:                                                                               
    #     break
    print(cnt)
    sentence = line.text
    origin_label = line.label
    predict_label = get_classfication_probabilities(sentence)  # 这里可以对每一条数据进行你需要的操作
    print(origin_label)
    print(predict_label)
    print("\n")
    if origin_label == predict_label:
      same_cnt += 1

print(same_cnt)
