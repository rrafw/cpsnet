import config
from urllib.request import urlopen
from bs4 import BeautifulSoup
import scrapy


class cpsnetFetch(scrapy.Spider):

    name = 'cpsnetFetch'
    allowed_domains = ['comprasnet.gov.br']

    date = '26/07/2018'

    def start_requests(self, date=date):
        pagina = 1
        while pagina < 40:   
        #for pagina in range(25,28):
            url = 'http://comprasnet.gov.br/ConsultaLicitacoes/ConsLicitacao_Relacao.asp?dt_publ_ini='+ date +'&dt_publ_fim='+ date +'&chkModalidade=1,2,3,20,5,99&chk_concor=31,32,41,42&chk_pregao=1,2,3,4&chk_rdc=1,2,3,4&optTpPesqMat=M&optTpPesqServ=S&chkTodos=-1&chk_concorTodos=-1&chk_pregaoTodos=-1&numpag='+ str(pagina)
            yield scrapy.Request(url=url, callback=self.parse, meta={'url': url, 'pagina': pagina})
            page = urlopen(url).read()
            soup = BeautifulSoup(page, features="lxml")
            form = soup.find('form')
            if form is not None:
                yield scrapy.Request(url=url, callback=self.parse, meta={'url': url, 'pagina': pagina})
            else:
                break            
            pagina += 1
        
            
    def parse(self, response, date=date):
        
        #form = response.xpath('//form').extract_first()
        day = date.split("/")
        filename = 'cpsnetFetch_dia' + day[0] + day[1] + day[2] + '_pagina' + str(response.meta['pagina']) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

            

            
            


    