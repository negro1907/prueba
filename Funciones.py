def devolver_top_n_variacion(df, n=10):
  data = df . copy()
  data["variacion"]  = data["Close"].pct_change() * 100 
  return data.sort_values("variacion", ascending=False).head(n)
  
  
  
