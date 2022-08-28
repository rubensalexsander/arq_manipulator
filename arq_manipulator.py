def list_to_arq(lt):
    return [str(i)+'\n' for i in lt]   

class Arq_txt:
    def __init__(self, local_file):
        self.local_file = local_file
    
    def connect(self, open_form='r'):
        try:
            arq = open(self.local_file, open_form)
            return arq
        except: return False
    
    def desconnect(self, arq):
        arq.close()

    def lines(self):
        arq = self.connect('r')
        self.lines = arq.readlines()
        self.desconnect(arq)
        return self.lines
    
    def rewrite_all(self, content=['']):
        arq = self.connect('w')
        arq.writelines(content)
        self.desconnect(arq)
    
    def rewrite_line(self, content='', line=-1):
        arq = self.connect()
        last_content = arq.readlines()
        if (len(last_content) - line) < 1:
            for i in range((len(last_content) - line)*-1+1):
                last_content.append('\n')      
        last_content[line] = content+'\n'
        new_content = last_content
        self.rewrite_all(new_content)
        self.desconnect(arq)

def main():
    print('txt_manipulate')

if __name__ == '__main__':
    main()
