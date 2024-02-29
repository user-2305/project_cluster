const data = require('./03-10_2022.json').values;

const myRegion = 'Воронежская область'

const myYear = 2019;

const hi = data.filter((element => element.region === myRegion && element.year === myYear))
console.log(hi)


function filtering(data) {

}