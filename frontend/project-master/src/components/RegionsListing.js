import Sort from "./Sort";
import Filtering from "./Filtering";
import {useState} from "react";

function RegionsListing({data, title}) {
    const [currentData, setNewData] = useState(data);
    const unit = data[0].unit;

    let unitForTable = '';
    if (data[0].unit.slice(-11) === 'в процентах') {
        unitForTable = '%';
    }

    //Индикатор для фильтрации
    const uniqueIndicators = () => {
        let uniqueArray = [];
        data.map(element => element.indicator in uniqueArray ? '' : uniqueArray.push(element.indicator))
        const uniqueIndicatorsForFiltering = Array(...new Set(uniqueArray));
        return uniqueIndicatorsForFiltering;
    }


    //Регионы для фильтрации
    const uniqueRegions = () => {
        let uniqueRegions = [];
        data.map(element => element.region in uniqueRegions ? '' : uniqueRegions.push(element.region))
        const regionsForFiltering = Array(...new Set(uniqueRegions));
        return regionsForFiltering;
    }

    //Федеральные округа для фильтрации
    const uniqueFederals = () => {
        let uniqueFed = [];
        data.map(element => element.fed_district in uniqueFed ? '' : uniqueFed.push(element.fed_district))
        const federalsForFiltering = Array(...new Set(uniqueFed));
        return federalsForFiltering;
    }

    const uniqueYears = () => {
        let uniqueYea = [];
        data.map(element => element.year in uniqueYea ? '' : uniqueYea.push(element.year))
        const yearsForFiltering = Array(...new Set(uniqueYea));
        return yearsForFiltering;
    }

    return (
        <>
            <h3 className="m-3">{title}</h3>
            <div className="flex-container">
                <div className="flex-item">
                    <Filtering filterOptions={uniqueRegions()} data={currentData}/>
                    <Filtering filterOptions={uniqueIndicators()} data={currentData}/>
                </div>
                <div className="flex-item">

                </div>
                <div className="flex-item">
                    <Sort/>
                </div>
            </div>
            <div className="body-for-table">
                <div className="table-responsive">
                    <table id='main' className="table table-striped table-bordered table-hover table-sm">
                        <thead>
                            <th>Название региона</th>
                            <th>Федеральный округ</th>
                            <th>Индикатор</th>
                            <th>Количество ({unit})</th>
                            <th>Год</th>
                        </thead>
                        <tbody>
                        {data.map(element => (
                                <tr key={element.id}>
                                    <td>{element.region}</td>
                                    <td>{element.fed_district}</td>
                                    <td>{element.indicator}</td>
                                    <td>{element.value}{unitForTable}</td>
                                    <td>{element.year}</td>
                                </tr>
                            )
                        )}
                        </tbody>
                    </table>
                </div>
            </div>
            ))
        </>
    )
};

export default RegionsListing;