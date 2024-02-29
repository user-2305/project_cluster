import {useState} from "react";

function IndicatorsBar(message) {
    const [activeIndicator, setActiveIndicator] = useState(1);

    return (
        <>
            <table>
                <tr>
                    <td><button className='btn active' onClick={() => setActiveIndicator(1)}>Муниципальные образования</button></td>
                    <td><button className='btn' onClick={() => setActiveIndicator(2)}>Сельхоз</button></td>
                    <td><button className='btn' onClick={() => setActiveIndicator(3)}>Уровень занятости населения</button></td>
                    <td><button className='btn' onClick={() => setActiveIndicator(4)}>Индикатор 4</button></td>
                    <td><button className='btn' onClick={() => setActiveIndicator(5)}>Индикатор 5</button></td>
                    <td><button className='btn' onClick={() => setActiveIndicator(6)}>Индикатор 6</button></td>
                </tr>
            </table>
        </>
    );
};

export default IndicatorsBar;