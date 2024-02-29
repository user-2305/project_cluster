import {useState} from "react";

function Sort() {
    const [sortingOption, setSortingOption] = useState(0);

    return (
        <>
            <h4>Сортировка</h4>
            <select className="form-select form-select-lg m-3">
                <option>Название региона</option>
                <option>Федеральный округ</option>
                <option>Индикатор</option>
                <option>Количество</option>
                <option>Год</option>
            </select>

            <input type='date' className='form-control' min={1980} max={2023}/>
        </>
    )
}
export default Sort;