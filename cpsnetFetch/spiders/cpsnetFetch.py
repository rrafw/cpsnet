import scrapy

class cpsnetFetch(scrapy.Spider):

    name = 'cpsnetFetch'
    allowed_domains = ['comprasnet.gov.br']

    date = '26/07/2018'
    checkForm = 1

    def start_requests(self, date=date):
        #pagina = 40
        
        #while (checkForm["check"] == True):   
        for pagina in range(24,30):
            
            global checkForm
            return checkForm
            if (checkForm == 1):
                url = 'http://comprasnet.gov.br/ConsultaLicitacoes/ConsLicitacao_Relacao.asp?dt_publ_ini='+ date +'&dt_publ_fim='+ date +'&chkModalidade=1,2,3,20,5,99&chk_concor=31,32,41,42&chk_pregao=1,2,3,4&chk_rdc=1,2,3,4&optTpPesqMat=M&optTpPesqServ=S&chkTodos=-1&chk_concorTodos=-1&chk_pregaoTodos=-1&numpag='+ str(pagina)
                yield scrapy.Request(url=url, callback=self.parse, meta={'url': url, 'pagina': pagina})
                print(pagina)
                #pagina += 1
            else:
                break
        
            
    def parse(self, response, date=date):
        
        form = response.xpath('//form').extract_first()
        if form is not None:
            day = date.split("/")
            filename = 'cpsnetFetch_dia' + day[0] + day[1] + day[2] + '_pagina' + str(response.meta['pagina']) + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            print('SSSSSSSSSSSSSSSSSSSSSSSSSSS')
        else:
            global checkForm
            checkForm = 0
            print('NNNNNNNNNNNNNNNNNNNNNNNNNN')

    