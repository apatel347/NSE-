from nsetools import Nse
import pandas as pd
from urllib.request import urlopen
import os
from tkinter import *
from tkinter import ttk
import _thread as th
import time
from datetime import datetime
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def StockNSE():
def StockDetails(symbol=&#39;nifty50&#39;):
stockWindow=Tk()
StockFrame=Frame(stockWindow, width=1300, height=600)
StockFrame.place(x=0, y=0)
StockFrame1 = Frame(stockWindow, width=1333, height=600,
bg=&#39;blue&#39;)
StockFrame1.place(x=0, y=28)

Label(StockFrame,text=&#39;Name&#39;, width=17, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=0)
Label(StockFrame,text=&#39;Open&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=1)
Label(StockFrame,text=&#39;High&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=2)
Label(StockFrame,text=&#39;Low&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0,column=3)
Label(StockFrame,text=&#39;Prv.Close&#39;, width=8, font=&#39;arial
14 bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0,column=4)
Label(StockFrame,text=&#39;LTP&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=5)
Label(StockFrame,text=&#39;CHNG&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=6)
Label(StockFrame,text=&#39;%CHNG&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=7)
Label(StockFrame,text=&#39;Volume&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=8)
Label(StockFrame,text=&#39;Value&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=9)
Label(StockFrame,text=&#39;52WH&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=10)

Label(StockFrame,text=&#39;52WL&#39;, width=8, font=&#39;arial 14
bold&#39;, bg=&#39;green&#39;, fg=&#39;red&#39;).grid(row=0, column=11)
r=1
for key in Nifty50Symbol:
q = Nse_data.get_quote(key)
Label(StockFrame1, text=key, width=22, font=&#39;arial
12&#39;).grid(row=r, column=0)
Label(StockFrame1, text=q[&#39;open&#39;], width=11,
font=&#39;arial 12&#39;).grid(row=r, column=1)
Label(StockFrame1, text=q[&#39;dayHigh&#39;],width=11,
font=&#39;arial 12&#39;).grid(row=r, column=2)
Label(StockFrame1, text=q[&#39;dayLow&#39;], width=11,
font=&#39;arial 12&#39;).grid(row=r, column=3)
Label(StockFrame1, text=q[&#39;previousClose&#39;],
width=11, font=&#39;arial 12&#39;).grid(row=r, column=4)
Label(StockFrame1, text=q[&#39;lastPrice&#39;], width=11,
font=&#39;arial 12&#39;).grid(row=r, column=5)
Label(StockFrame1, text=q[&#39;change&#39;], width=10,
font=&#39;arial 12&#39;).grid(row=r, column=6)
Label(StockFrame1, text=q[&#39;pChange&#39;], width=10,
font=&#39;arial 12&#39;).grid(row=r, column=7)
Label(StockFrame1, text=q[&#39;totalTradedVolume&#39;],
width=11, font=&#39;arial 12&#39;).grid(row=r, column=8)
Label(StockFrame1, text=q[&#39;totalTradedValue&#39;],
width=11, font=&#39;arial 12&#39;).grid(row=r, column=9)
Label(StockFrame1, text=q[&#39;high52&#39;], width=10,
font=&#39;arial 12&#39;).grid(row=r, column=10)
Label(StockFrame1, text=q[&#39;low52&#39;], width=10,
font=&#39;arial 12&#39;).grid(row=r, column=11)
r+=1
stockWindow.title(&#39;NSE Details&#39;)
stockWindow.geometry(&quot;1350x650&quot;)
stockWindow.mainloop()
def ReadSymbol():
global Nifty50Symbol, Niftynext50Symbol, Nifty100Symbol,
Niftymidcap50Symbol, NiftyBankSymbol
if not os.path.exists(&#39;ind_nifty50list.csv&#39;):
url =
&#39;https://archives.nseindia.com/content/indices/ind_nifty50list.c
sv&#39;
fs = urlopen(url)
df = pd.read_csv(fs)
Nifty50Symbol = df[&#39;Symbol&#39;].tolist()
df.to_csv(&#39;ind_nifty50list.csv&#39;)
else:
df=pd.read_csv(&#39;ind_nifty50list.csv&#39;)
Nifty50Symbol=df[&#39;Symbol&#39;].tolist()

if not os.path.exists(&#39;ind_nifty100list.csv&#39;):
url =
&#39;https://archives.nseindia.com/content/indices/ind_nifty100list.
csv&#39;
fs = urlopen(url)
df = pd.read_csv(fs)
Nifty100Symbol = df[&#39;Symbol&#39;].tolist()
df.to_csv(&#39;ind_nifty100list.csv&#39;)
else:
df=pd.read_csv(&#39;ind_nifty100list.csv&#39;)
Nifty100Symbol=df[&#39;Symbol&#39;].tolist()
if not os.path.exists(&#39;ind_niftynext50list.csv&#39;):
url =
&#39;https://archives.nseindia.com/content/indices/ind_niftynext50li
st.csv&#39;
fs = urlopen(url)
df = pd.read_csv(fs)
Niftynext50Symbol = df[&#39;Symbol&#39;].tolist()
df.to_csv(&#39;ind_niftynext50list.csv&#39;)
else:
df=pd.read_csv(&#39;ind_niftynext50list.csv&#39;)
Niftynext50Symbol=df[&#39;Symbol&#39;].tolist()
if not os.path.exists(&#39;ind_niftymidcap50list.csv&#39;):
url =
&#39;https://archives.nseindia.com/content/indices/ind_niftymidcap50
list.csv&#39;
fs = urlopen(url)
df = pd.read_csv(fs)
Niftymidcap50Symbol = df[&#39;Symbol&#39;].tolist()
df.to_csv(&#39;ind_niftymidcap50list.csv&#39;)
else:
df=pd.read_csv(&#39;ind_nifty50list.csv&#39;)
Niftymidcap50Symbol=df[&#39;Symbol&#39;].tolist()
if not os.path.exists(&#39;ind_niftybanklist.csv&#39;):
df = pd.DataFrame(data=None, columns=[&#39;Symbol&#39;,
&#39;Name&#39;])
all_stock_codes =
Nse_data.get_stock_codes(cached=False)
for key in all_stock_codes:
if &#39;BANK&#39; in all_stock_codes[key].upper():
df = df.append({&#39;Symbol&#39;: key, &#39;Name&#39;:
all_stock_codes[key]}, ignore_index=True)
NiftyBankSymbol = df[&#39;Symbol&#39;].tolist()
df.to_csv(&#39;ind_niftybanklist.csv&#39;)
else:
df=pd.read_csv(&#39;ind_niftybanklist.csv&#39;)
NiftyBankSymbol=df[&#39;Symbol&#39;].tolist()

def widget():
global Nifty50Btn, Niftynxt50Btn, Nifty100Btn,
Niftymidcap50Btn, NiftyBankBtn, Toptrv, Bottomtrv, graph
F1 = Frame(window, height=100)
Nifty50Btn = Button(F1, text=&#39;NIFTY 50&#39;, image=dnArrow,
compound=BOTTOM, bg=&#39;white&#39;, activebackground=&#39;white&#39;,
activeforeground=&#39;red&#39;, fg=&#39;Blue&#39;,
font=&#39;Arial 12 bold&#39;, width=160, command=setTimer)
Nifty50Btn.place(x=5, y=5)
Nifty100Btn = Button(F1, text=&#39;NIFTY 100&#39;,
image=dnArrow, compound=BOTTOM, bg=&#39;white&#39;, fg=&#39;Blue&#39;,
activebackground=&#39;white&#39;,
activeforeground=&#39;red&#39;, font=&#39;Arial 12 bold&#39;, width=160,
command=lambda :setTimer(&#39;nifty100&#39;))
Nifty100Btn.place(x=170, y=5)
Niftynxt50Btn = Button(F1, text=&#39;NIFTY NEXT 50&#39;,
image=dnArrow, compound=BOTTOM, bg=&#39;white&#39;, fg=&#39;Blue&#39;,
activebackground=&#39;white&#39;,
activeforeground=&#39;red&#39;, font=&#39;Arial 12 bold&#39;, width=160,
command=lambda :setTimer(&#39;niftynext50&#39;))
Niftynxt50Btn.place(x=335, y=5)
Niftymidcap50Btn = Button(F1, text=&#39;NIFTY MIDCAP 50&#39;,
image=dnArrow, compound=BOTTOM, bg=&#39;white&#39;, fg=&#39;Blue&#39;,
activebackground=&#39;white&#39;,
activeforeground=&#39;red&#39;, font=&#39;Arial 12 bold&#39;, width=160,
command=lambda : setTimer(&#39;niftymidcap50&#39;))
Niftymidcap50Btn.place(x=500, y=5)
NiftyBankBtn = Button(F1, text=&#39;NIFTY BANK&#39;,
image=dnArrow, compound=BOTTOM, bg=&#39;white&#39;, fg=&#39;Blue&#39;,
activebackground=&#39;white&#39;,
activeforeground=&#39;red&#39;, font=&#39;Arial 12 bold&#39;, width=160,
command=lambda :setTimer(&#39;niftybank&#39;))
NiftyBankBtn.place(x=665, y=5)
# F1.pack(fill=&quot;x&quot;, expand=&#39;yes&#39;, padx=10, pady=10)
# F2.pack(fill=&quot;both&quot;, expand=&#39;yes&#39;, padx=10, pady=10)
# F3.pack(fill=&quot;both&quot;, expand=&#39;yes&#39;, padx=10, pady=10)
F2 = Frame(window, bg=&#39;yellow&#39;)
F21 = LabelFrame(F2, text=&quot;TOP GAINER&quot;, bg=&#39;green&#39;)
F22 = LabelFrame(F2, text=&quot;TOP LOSER&quot;, bg=&#39;red&#39;)
Toptrv = ttk.Treeview(F21, columns=(1, 2, 3, 4),
show=&quot;headings&quot;, height=&#39;5&#39;)

Toptrv.pack(fill=&#39;both&#39;, expand=&#39;yes&#39;, padx=&#39;5&#39;,
pady=&#39;5&#39;)
Toptrv.column(1, width=150)
Toptrv.column(2, width=80)
Toptrv.column(3, width=80)
Toptrv.column(4, width=80)
Toptrv.heading(1, text=&quot;SYMBOL&quot;)
Toptrv.heading(2, text=&quot;LTP&quot;)
Toptrv.heading(3, text=&quot;%CHNG&quot;)
Toptrv.heading(4, text=&quot;VOLUME&quot;)
Bottomtrv = ttk.Treeview(F22, columns=(1, 2, 3, 4),
show=&quot;headings&quot;, height=&#39;5&#39;)
Bottomtrv.pack(fill=&#39;both&#39;, expand=&#39;yes&#39;, padx=&#39;5&#39;,
pady=&#39;5&#39;)
Bottomtrv.column(1, width=150)
Bottomtrv.column(2, width=80)
Bottomtrv.column(3, width=80)
Bottomtrv.column(4, width=80)
Bottomtrv.heading(1, text=&quot;SYMBOL&quot;)
Bottomtrv.heading(2, text=&quot;LTP&quot;)
Bottomtrv.heading(3, text=&quot;%CHNG&quot;)
Bottomtrv.heading(4, text=&quot;VOLUME&quot;)
F21.grid(row=0, column=0, padx=5, pady=5, sticky=&#39;nesw&#39;)
F22.grid(row=0, column=1, padx=5, pady=5, sticky=&#39;nesw&#39;)
F3 = Frame(window, bg=&#39;light blue&#39;)
f = Figure(figsize=(5, 5), dpi=100)
graph = f.add_subplot(111)
df=pd.read_csv(&#39;TimewiseStock.csv&#39;)
Timev=df[&#39;Time&#39;].tolist()
datav=df[&#39;StockValue&#39;].tolist()
#f.align_xlabels([&#39;9:00&#39;,&#39;10:00&#39;, &#39;11:00&#39;,&#39;12:00&#39;,
&#39;13:00&#39;, &#39;14:00&#39;,&#39;15:00&#39;])
graph.plot(Timev,datav)
canvas = FigureCanvasTkAgg(f, F3)
canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH,
expand=True)
Nifty50DailyQuote = Nse_data.get_index_quote(&quot;nifty 50&quot;)
Nifty50Btn[&#39;text&#39;] = &#39;NIFTY 50\n&#39; +
str(Nifty50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; + str(
Nifty50DailyQuote[&#39;change&#39;]) + &#39; (&#39; + str(
Nifty50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Nifty50DailyQuote[&#39;pChange&#39;]) &gt; 0:
Nifty50Btn[&#39;image&#39;] = upArrow
else:
Nifty50Btn[&#39;image&#39;] = dnArrow

Nifty100DailyQuote = Nse_data.get_index_quote(&quot;nifty
100&quot;)
Nifty100Btn[&#39;text&#39;] = &#39;NIFTY 100\n&#39; +
str(Nifty100DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; + str(
Nifty100DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Nifty100DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Nifty100DailyQuote[&#39;pChange&#39;]) &gt; 0:
Nifty100Btn[&#39;image&#39;] = upArrow
else:
Nifty100Btn[&#39;image&#39;] = dnArrow
Niftynxt50DailyQuote = Nse_data.get_index_quote(&quot;nifty
next 50&quot;)
Niftynxt50Btn[&#39;text&#39;] = &#39;NIFTY NEXT 50\n&#39; +
str(Niftynxt50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; + str(
Niftynxt50DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Niftynxt50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Niftynxt50DailyQuote[&#39;pChange&#39;]) &gt; 0:
Niftynxt50Btn[&#39;image&#39;] = upArrow
else:
Niftynxt50Btn[&#39;image&#39;] = dnArrow
Niftymidcap50DailyQuote =
Nse_data.get_index_quote(&quot;NIFTY MIDCAP 50&quot;)
Niftymidcap50Btn[&#39;text&#39;] = &#39;NIFTY MIDCAP 50\n&#39; +
str(Niftymidcap50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; + str(
Niftymidcap50DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Niftymidcap50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Niftymidcap50DailyQuote[&#39;pChange&#39;]) &gt; 0:
Niftymidcap50Btn[&#39;image&#39;] = upArrow
else:
Niftymidcap50Btn[&#39;image&#39;] = dnArrow
NiftyBankDailyQuote = Nse_data.get_index_quote(&quot;NIFTY
BANK&quot;)
NiftyBankBtn[&#39;text&#39;] = &#39;NIFTY BANK\n&#39; +
str(NiftyBankDailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; + str(
NiftyBankDailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(NiftyBankDailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(NiftyBankDailyQuote[&#39;pChange&#39;]) &gt; 0:
NiftyBankBtn[&#39;image&#39;] = upArrow
else:
NiftyBankBtn[&#39;image&#39;] = dnArrow
top_gainers = Nse_data.get_top_gainers()
c = 0
for i in top_gainers:
if i[&#39;symbol&#39;] in Nifty50Symbol:
c += 1

Toptrv.insert(&#39;&#39;, &#39;end&#39;, values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
top_loser = Nse_data.get_top_losers()
c = 0
for i in top_loser:
if i[&#39;symbol&#39;] in Nifty50Symbol:
c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;, values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break

F4 = Frame(window, bg=&#39;light blue&#39;)
B1=Button(F4,text=&#39;Details&#39;, command=StockDetails)
B1.pack()
F1.place(x=5, y=2, width=835, height=100)
F2.place(x=5, y=105, width=835, height=165)
F3.place(x=5, y=270, width=835, height=300)
F4.place(x=5, y=570, width=835, height=100)

def setTimer(symbol=&#39;nifty50&#39;):
now = datetime.now()
current_time = now.strftime(&quot;%H:%M:%S&quot;)
if (now.strftime(&quot;%A&quot;)not in [&#39;Saturday&#39;, &#39;Sunday&#39;]) and
(float(current_time[:2] + &#39;.&#39; + current_time[3:5]) &gt;= 9.0 and
float(current_time[:2] + &#39;.&#39; + current_time[3:5]) &lt; 15.30):
th.start_new_thread(fetchData,
(current_time,symbol))
else:
fetchData(s=symbol)

def fetchData(t=&#39;&#39;,s=&#39;nifty50&#39;):
print(t,s)
for i in Toptrv.get_children():
Toptrv.delete(i)
for i in Bottomtrv.get_children():
Bottomtrv.delete(i)
top_gainers = Nse_data.get_top_gainers()
c = 0
for i in top_gainers:
if s == &#39;nifty50&#39;:
if i[&#39;symbol&#39;] in Nifty50Symbol:
c += 1
Toptrv.insert(&#39;&#39;, &#39;end&#39;,

values=(i[&#39;symbol&#39;], i[&#39;ltp&#39;], i[&#39;netPrice&#39;],
i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftynext50&#39;:
if i[&#39;symbol&#39;] in Niftynext50Symbol:
c += 1
Toptrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;], i[&#39;ltp&#39;], i[&#39;netPrice&#39;],
i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;nifty100&#39;:
if i[&#39;symbol&#39;] in Nifty100Symbol:
c += 1
Toptrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;], i[&#39;ltp&#39;], i[&#39;netPrice&#39;],
i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftymidcap50&#39;:
if i[&#39;symbol&#39;] in Niftymidcap50Symbol:
c += 1
Toptrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;], i[&#39;ltp&#39;], i[&#39;netPrice&#39;],
i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftybank&#39;:
if i[&#39;symbol&#39;] in NiftyBankSymbol:
c += 1
Toptrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;], i[&#39;ltp&#39;], i[&#39;netPrice&#39;],
i[&#39;tradedQuantity&#39;]))
if c == 5:
break
top_loser = Nse_data.get_top_losers()
c = 0
for i in top_loser:
if s == &#39;nifty50&#39;:
if i[&#39;symbol&#39;] in Nifty50Symbol:
c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftynext50&#39;:
if i[&#39;symbol&#39;] in Niftynext50Symbol:

c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;nifty100&#39;:
if i[&#39;symbol&#39;] in Nifty100Symbol:
c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftymidcap50&#39;:
if i[&#39;symbol&#39;] in Niftymidcap50Symbol:
c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
elif s == &#39;niftybank&#39;:
if i[&#39;symbol&#39;] in NiftyBankSymbol:
c += 1
Bottomtrv.insert(&#39;&#39;, &#39;end&#39;,
values=(i[&#39;symbol&#39;],
i[&#39;ltp&#39;], i[&#39;netPrice&#39;], i[&#39;tradedQuantity&#39;]))
if c == 5:
break
#graph.plot()
if t!=&#39;&#39; and (float(t[:2]+&#39;.&#39;+t[3:5])&gt;=9.0 and
float(t[:2]+&#39;.&#39;+t[3:5])&lt;15.30):
#print(float(t[:2]+&#39;.&#39;+t[3:5]))
while True:
Nifty50DailyQuote =
Nse_data.get_index_quote(&quot;nifty 50&quot;)
Nifty50Btn[&#39;text&#39;] = &#39;NIFTY 50\n&#39; +
str(Nifty50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; +
str(Nifty50DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Nifty50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Nifty50DailyQuote[&#39;pChange&#39;]) &gt; 0:
Nifty50Btn[&#39;image&#39;] = upArrow
else:
Nifty50Btn[&#39;image&#39;] = dnArrow
Nifty100DailyQuote =
Nse_data.get_index_quote(&quot;nifty 100&quot;)
Nifty100Btn[&#39;text&#39;] = &#39;NIFTY 100\n&#39; +

str(Nifty100DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; +
str(Nifty100DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Nifty100DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Nifty100DailyQuote[&#39;pChange&#39;]) &gt; 0:
Nifty100Btn[&#39;image&#39;] = upArrow
else:
Nifty100Btn[&#39;image&#39;] = dnArrow
Niftynxt50DailyQuote =
Nse_data.get_index_quote(&quot;nifty next 50&quot;)
Niftynxt50Btn[&#39;text&#39;] = &#39;NIFTY NEXT 50\n&#39; +
str(Niftynxt50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; +
str(Niftynxt50DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Niftynxt50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Niftynxt50DailyQuote[&#39;pChange&#39;]) &gt; 0:
Niftynxt50Btn[&#39;image&#39;] = upArrow
else:
Niftynxt50Btn[&#39;image&#39;] = dnArrow
Niftymidcap50DailyQuote =
Nse_data.get_index_quote(&quot;NIFTY MIDCAP 50&quot;)
Niftymidcap50Btn[&#39;text&#39;] = &#39;NIFTY MIDCAP 50\n&#39; +
str(Niftymidcap50DailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; +
str(Niftymidcap50DailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(Niftymidcap50DailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(Niftymidcap50DailyQuote[&#39;pChange&#39;]) &gt;
0:
Niftymidcap50Btn[&#39;image&#39;] = upArrow
else:
Niftymidcap50Btn[&#39;image&#39;] = dnArrow
NiftyBankDailyQuote =
Nse_data.get_index_quote(&quot;NIFTY BANK&quot;)
NiftyBankBtn[&#39;text&#39;] = &#39;NIFTY BANK\n&#39; +
str(NiftyBankDailyQuote[&#39;lastPrice&#39;]) + &#39;\n&#39; +
str(NiftyBankDailyQuote[&#39;change&#39;]) + &#39; (&#39; +
str(NiftyBankDailyQuote[&#39;pChange&#39;]) + &#39;%)&#39;
if float(NiftyBankDailyQuote[&#39;pChange&#39;]) &gt; 0:
NiftyBankBtn[&#39;image&#39;] = upArrow
else:
NiftyBankBtn[&#39;image&#39;] = dnArrow
#graph.plot()
time.sleep(1)

Nse_data = Nse()
window = Tk()

window.title(&#39;NSE&#39;)
window.geometry(&quot;850x650&quot;)
upArrow=ImageTk.PhotoImage(Image.open(&#39;uparrow.png&#39;).resize((25,
25)))
dnArrow=ImageTk.PhotoImage(Image.open(&#39;downarrow.png&#39;).resize((2
5,25)))
ReadSymbol()
widget()
fetchData()
window.mainloop()
if __name__==&#39;__main__&#39;:
StockNSE()