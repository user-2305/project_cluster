import './App.css';
import RegionsListing from "./components/RegionsListing";
import {useState} from "react";

const data1 = require('./data/01-06_2022new.json').values;
const title1 = require('./data/01-06_2022new.json').section;
const data2 = require('./data/12-20_2022.json').values;
const data3 = require('./data/03-10_2022.json').values;

function changeableDataBlock(indicator) {
    switch (indicator) {
        case 1:
            return <RegionsListing data={data1} title='Муниципальные образования'/>
        case 2:
            return <RegionsListing data={data2} title='Сельскохозяйственные индикаторы'/>
        case 3:
            return <RegionsListing data={data3} title='Население' measure = '%'/>
    };
}
function App() {
    const [activeIndicator, setActiveIndicator] = useState(1);

    return (
          <>
              <h1>Таблицы базы данных</h1>
              <h3>{title1}</h3>
              <table className="indicators-bar">
                  <tr>
                      <td><button className='btn' onClick={() => setActiveIndicator(1)}>Муниципальные образования</button></td>
                      <td><button className='btn' onClick={() => setActiveIndicator(2)}>Сельхоз</button></td>
                      <td><button className='btn' onClick={() => setActiveIndicator(3)}>Уровень занятости населения</button></td>
                  </tr>
              </table>
              {changeableDataBlock(activeIndicator)}
          </>
        );
}

export default App;
