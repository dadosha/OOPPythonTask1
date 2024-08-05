import json
import os


def json_open_file(file_path):
    file_path = os.path.join(os.getcwd(), file_path)

    with open(file_path, encoding="UTF-8") as f:
        json_file = json.load(f)

    return json_file


def get_all_news_text(json_file):
    news_list = json_file["rss"]["channel"]["items"]
    news_text_list = []
    for news in news_list:
        news_text_list.append(news["description"])
        news_text_list.append(news["title"])

    return news_text_list


def parsing_text(news_text_list):
    words_dict = {}
    for news_text in news_text_list:
        words_list = news_text.split(" ")
        for word in words_list:
            if word in words_dict:
                words_dict[word] += 1
            elif len(word) > 6:
                words_dict[word] = 1
    sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_words


def print_more_count_word(words_count):
    for word in words_count[:10]:
        print(word[0] + " - " + str(word[1]))


def main():
    file_path = '../files/newsafr.json'
    json_file = json_open_file(file_path)
    news_text_list = get_all_news_text(json_file)
    words_count = parsing_text(news_text_list)
    print_more_count_word(words_count)


if __name__ == "__main__":
    main()
