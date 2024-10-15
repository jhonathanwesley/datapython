# pip install yfinance
import yfinance as yf
import matplotlib.pyplot as mplt

acoes = ['AAPL', 'MSFT', 'PETR4.SA', 'BBDC4.SA']

dados_acoes = yf.download(acoes,
                          period = '1d',
                          start = '2022-01-01')

dados_acoes['Close'].plot()
mplt.xlabel('Data')
mplt.ylabel('Preço de Fechamento')
mplt.title('Rastreador de ações')
mplt.legend(acoes, fontsize = 8)
mplt.show()

dados_normalizados = dados_acoes['Close'] / dados_acoes['Close'].iloc[0]
dados_normalizados.plot()
mplt.xlabel('Data')
mplt.ylabel('Preço Normalizado')
mplt.title('Rastreador de ações')
mplt.legend(acoes, fontsize = 8)
mplt.show()