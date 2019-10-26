'''enum TokenType {                                   
  // Single-character tokens.                      
  LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
  COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR, 

  // One or two character tokens.                  
  BANG, BANG_EQUAL,                                
  EQUAL, EQUAL_EQUAL,                              
  GREATER, GREATER_EQUAL,                          
  LESS, LESS_EQUAL,                                

  // Literals.                                     
  IDENTIFIER, STRING, NUMBER,                      

  // Keywords.                                     
  AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,  
  PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,    

  EOF                                              
}'''

#Necessario definir a classe dos tokens, que contem as seguintes informações sobre o token
#tipo, lexema, valor literal e linha

class Token:

    def __init__(self, type, lexeme, literal, line):
        self.tipo = type
        self.lexema = lexeme
        self.literal = literal
        self.linha = line

    def __str__(self):
        return str(self.tipo)+", "+str(self.lexema)+", "+str(self.literal)+", "+str(self.linha)

class Token:

    def __init__(self, tipo, lexema, literal, linha):
        self.tipo = tipo
        self.lexema = lexema
        self.literal = literal
        self.linha = linha

    def __str__(self):
        return str(self.tipo)+" "+str(self.lexema)+" "+str(self.literal)+" "+str(self.linha)

#classe do Scanner, que sera usado para percorrer a entrada e pegar todos os tokens existentes
#string = o codigo fonte bruto que sera lido, listaTokens = uma lista que será preenchida com os
#tokens encontrados, comeco e atual são posições dos caracteres presentes nos lexemas sendo analisados

class Scanner:

    def __init__(self, string):
        self.string = string
        self.listaTokens = []
        self.comeco = 0
        self.atual = 0
        self.linha = 1

    #final eh uma função que nos diz se todos os caracteres do lexema já foram checados
    def final(self):
        return self.atual >= len(self.string)

    def scanTokens(self):
        while(not self.final()):
            self.comeco = self.atual
            self.scanTokens()
            
    def scanToken(self):
        c = self.avancar()

        if c == '(':
            self.addToken("PAREN_ESQ")
        elif c == ')':
            self.addToken("PAREN_DIR")
        elif c == '{':
            self.addToken("CHAVE_ESQ")
        elif c == '}':
            self.addToken("CHAVE_DIR")
        elif c == ',':
            self.addToken("VIRGULA")
        elif c == '.':
            self.addToken("PONTOFINAL")
        elif c == '-':
            self.addToken("MENOS")
        elif c == '+':
            self.addToken("MAIS")
        elif c == ';':
            self.addToken("PONTOVIRGULA")
        elif c == '*':
            self.addToken("MULTIPLICACAO")
        elif c == '!':
            if self.match('='):
                self.addToken("DIFERENTE")
            else:
                self.addToken("NEGACAO")
        elif c == '=':
            if self.match('='):
                self.addToken("COMPARADORIGUAL")
            else:
                self.addToken("ATRIBUCAO")
        elif c == '<':
               if self.match('='):
                   self.addToken("MENORIGUAL")
                else:
                    self.addToken("MENORQUE")
        elif c == '>':
            if self.match('='):
                self.addToken("MAIORIGUAL")
            else:
                self.addToken("MAIORQUE")

        else:
            print("Erro na linha", self.linha, "Caractere", c, "invalido")
            raise Exception()

        def match(self, esperado):
            if self.final():
                return False
            elif self.string[self.atual] != esperado:
                return False

            self.atual = self.atual + 1
            return True

        def avancar(self):
            self.atual = self.atual + 1
            return self.string[self.atual - 1]

        def addToken(self, tipo, literal):
            literal = None
            string2 = self.string[self.comeco:self.atual]
            self.listaTokens.append(Token(tipo,string2,literal,self.linha))
    
