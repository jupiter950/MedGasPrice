import React, { useEffect, useState } from 'react';
import './App.css';
import useWebSocket, { ReadyState } from 'react-use-websocket';
import ReactTableUI from 'react-table-ui';
import axios from 'axios';

type DataType = {
  date: string,
  price: number
}

function App() {
  const { sendMessage, lastMessage } = useWebSocket(process.env.SOCKET_URL || 'ws://127.0.0.1:8000/ws/test/')
  const [ medPrice, setMedPrice ] = useState<number>(0)
  const [ data, setData ] = useState<DataType[]>([])
  const [ isLoading, setIsLoading ] = useState<boolean>(false)

  useEffect(() => {
    setIsLoading(true)
    axios.get("http://127.0.0.1:8000/api/gasprices").then(res => {
      console.log(res.data);
      const data = res.data.map((item: any) => {
        const date = new Date(item.price_date)

        return ({
          'date': item.price_date,
          'price' : Math.floor(parseInt(item.price) / 1000000000)
        })
      })
      setData(data)
    })
    axios.get("http://127.0.0.1:8000/api/medprice").then(res => {
      console.log(res.data);
      setMedPrice(parseInt(res.data[0].low))
    })
    setIsLoading(false)
  },[lastMessage])

  return (
    <div className="App container">
      {
        isLoading && (
          <>
            <div className="loader"></div>
            <div className='background'></div>  
          </>
        )
      }
      <p className='text-center lg-font'>Med Gas Price: <span className='color-green'>{ medPrice && medPrice}</span> nAVAX</p>
      {
        data && (
          <ReactTableUI data={data} title="gas price" />
        )
      }
    </div>
  );
}

export default App;
