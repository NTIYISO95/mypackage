#from mypackage.includes import constants
import pandas as pd
import numpy as np



# dictionary mapping official municipality twitter handles to the municipality name

mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

# Function 1:

### START FUNCTION
def dictionary_of_metrics(items:list):
    itemsort = sorted(items)
    return {"mean": round(np.mean(items),2),
            "median": round(np.median(items),2),
            "std": round(np.std(items, ddof=1),2),
            "var": round(np.var(items, ddof=1),2),
            "min": itemsort[0],
            "max": itemsort[-1]}
### END FUNCTION

# Function 2:

### START FUNCTION
def five_num_summary(items:list):
    sorteditems = sorted(items)
    return {'max': sorteditems[-1],
            'median': round(np.median(items),2) ,
            'min': sorteditems[0],
            'q1': np.percentile(sorteditems, 25),
            'q3': np.percentile(sorteditems, 75)}
### END FUNCTION
# Function 3:

### START FUNCTION
def date_parser(dates:list):
    return [i.split(' ', 1)[0] for i in dates]
### END FUNCTION
# Funtion 4:

### START FUNCTION
def extract_municipality_hashtags(df,cities=mun_dict):
    contains_email = []
    hashtags = []
    for x in df["Tweets"]:
        contains_email.append([cities[i] for i in x.split(' ') if i in cities.keys()])
        hashtags.append([i.lower() for i in x.split(' ') if '#' in i])
    contains_email_nan = [i if i else np.nan for i in contains_email]
    hashtags_nan = [i if i else np.nan for i in hashtags]
    df["municipality"] = contains_email_nan
    df["hashtags"] = hashtags_nan
    return df
### END FUNCTION
# Funtion 5:

### START FUNCTION
def number_of_tweets_per_day(df):
    df["Date"] = [i.split(' ', 1)[0] for i in df["Date"]]
    a = sorted(list(df["Date"].unique()))
    dictp = {}
    for i in a:
        for x in df[df["Date"] == i]["Date"]:
            if x in dictp.keys():
                dictp[x] += 1
            else:
                dictp[x] = 1
    new_df = pd.DataFrame.from_dict(data=dictp, orient="index", columns=["Tweets"])
    new_df.index.name = "Date"
    return new_df
### END FUNCTION
# Funtion 6:

### START FUNCTION
def word_splitter(df):
    meh = [list(i.lower().split(" ")) for i in df["Tweets"]]
    df["Split Tweets"] = meh
    df['Date'] = [i.split(' ', 1)[0] for i in df["Date"]]
    df['Tweets'] = [i.lower() for i in df["Tweets"]]
    return df
### END FUNCTION
# Funtion 7:

### START FUNCTION
def stop_words_remover(df,stops=stop_words_dict):
    def hash_me(words):
        return [i for i in words.lower().split() if i not in stops["stopwords"]]

    df["Without Stop Words"] = df["Tweets"].apply(hash_me)
    return df   
### END FUNCTION



