# chart render import
import charts
# searching in the api
import json
import requests


# empty array for store the subreddits name
words = []
subreddits = []
data = []
count = 0


def dataCharts(word, subr, data):
    final_data = [subr, word, data]
    #print('final data: ', final_data)
    # calling render method
    charts.main(final_data)


def search(words, subreddits, data, count):
    # to every subreddit
    for word in range(len(words)):
        # to every word to search
        for sub in range(len(subreddits)):
            # initialize the url
            url = ('https://www.reddit.com/r/' +
                   subreddits[sub]+'/comments.json')
            request = requests.get(url, headers={'User-agent': 'your bot 0.1'})
            # gettin json object
            obj = request.json()

            for y in range(24):

                if 'body' in (obj['data']['children'][y]['data']):

                    body = obj['data']['children'][y]['data']['body']
                    text = body.split(' ')

                    for i in text:
                        if i == words[word]:

                            count += 1

                else:
                    print('section not found. JSON structure is different.')
                    break
        print(words[word], 'has been found ', count, ' times.')
        # add to data
        data.append(count)
    # print(data)  # array filled with data
    dataCharts(words, subreddits, data)


def main():
    # ask for the word to search
    num_words = int(input('Enter the words number that you want to search: '))
    # ask the number os subreddits that we want to search
    num_subreddits = int(input('How many subreddits i have to search in? '))

    if num_words == num_subreddits:
        for i in range(num_words):
            nameW = input('Enter word: ')
            # append names to the array
            words.append(nameW)

        for j in range(num_subreddits):
            nameS = input('Enter the subreddit: ')
            # append names to the array
            subreddits.append(nameS)

        search(words, subreddits, data, count)
    else:
        print('You must search the same number of words in the same number of subreddits!')
        exit()


if __name__ == "__main__":
    main()
