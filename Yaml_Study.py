import yaml

def loader(path):
    with open(path,"r") as desc:
        data =yaml.load(desc)
    return data

def y_dump(path,data):
    with open( path,"w") as desc:
        yaml.dump(data,desc)

if __name__=="__main__":
    path="a.YAML"
    data=loader(path)
    print(data)

    invoice = data['invoice']
    print(invoice)

    data = dict(
        A='a',
        B=dict(
            C='c',
            D='d',
            E='e',
        )
    )

    with open('data.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
