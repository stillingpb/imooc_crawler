# coding=utf-8
class Data_Outputer:
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html><head><meta charset="UTF-8"></head><body><table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td><a href="%s">' % data['url'])
            fout.write('%s</a></td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table></body></html>')
        fout.close()
