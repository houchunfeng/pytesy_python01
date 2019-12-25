import yaml

data_input = {'a': '1', 'b': '2', 'c': '3'}
with open("./sum.yml", "w", encoding='utf-8') as f:
    result = yaml.safe_dump(data_input, f, encoding='utf-8', allow_unicode=True)
    print(result)
    print(type(result))
