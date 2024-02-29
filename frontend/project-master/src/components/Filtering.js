import {useEffect, useState} from "react";
function Filtering(props) {
    const filterOptions = props.filterOptions;
    return (
        <>
            <select className="form-select form-select-lg m-3">
                {filterOptions.map(filter => <option><input type='checkbox' value={filter}/>{filter}</option>)}
            </select>
        </>
    )
}

export default Filtering;