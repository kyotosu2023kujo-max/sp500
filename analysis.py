import yfinance as yf
import matplotlib.pyplot as plt
import os

def save_sp500_chart():
    # データをダウンロード
    data = yf.download('^GSPC', period='1y')
    
    # グラフ作成
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], color='blue', label='S&P 500')
    
    # 25日移動平均線を追加 (データサイエンスの基本テク)
    data['MA25'] = data['Close'].rolling(window=25).mean()
    plt.plot(data.index, data['MA25'], color='orange', label='25Day MA')
    
    plt.title('S&P 500 Index with 25MA')
    plt.legend()
    plt.grid(True)
    
    # 画像として保存
    plt.savefig('sp500_latest.png')
    print("Chart updated!")

if __name__ == "__main__":
    save_sp500_chart()
