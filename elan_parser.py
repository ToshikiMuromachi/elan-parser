import xml.etree.ElementTree as ET


def read(path):
    with open(path) as f:
        xml_data = f.read()

    return ET.fromstring(xml_data)


if __name__ == '__main__':
    root = read('/home/toshiki/data/Chiba3Party/ELAN/chiba0132.eaf')
    # 最上位階層のタグと中身
    print(root.tag, root.attrib)

    print("--*--*--")

    # 子階層のタグと中身
    for child in root:
        print(child.tag, child.attrib)

    print("--*--*--")

    # テキスト抽出
    for annotation in root.iter('ANNOTATION_VALUE'):
        print(annotation.tag, annotation.text)

