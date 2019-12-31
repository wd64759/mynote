const express = require('express')
const  {buildSchema} = require('graphql')
const grapqlHTTP = require('express-graphql')

const schema = buildSchema(`
    type Query {
        job(typ: String!, salary: Int): [Job],
        city(code: String!): City,
        company(employer: String!): Company
    },
    type Job {
        name: String,
        typ: String,
        status: String,
        salary: Int,
        openDays: Int,
        employer: String,
        company(employer: String): Company
    },
    type Company {
        name: String,
        industry: String,
        size: Int,
        location: String,
        branch(code: String): [City]
    },
    type City {
        name: String,
        state: String,
        population: Float,
        code: String
    }
`)

const root = {    
    city: ({code}) => {
        const cities = [
            {'name': 'xian', 'state': 'Shan Xi', 'population': 6000000, 'code': '002'},
            {'name': 'shanghai', 'state': 'Shang Hai', 'population': 30000000, 'code': '001'},
            {'name': 'chengdu', 'state': 'Si Chuan', 'population': 4000000, 'code': '003'}
        ];
        console.log('call me >> [city]' + code)
        found = cities.find(e=>{ return e.code === code });
        return found;
    },
    company({employer} ) {
        const comps = [
            {name: 'Sony', industry: 'media', size: 10000, location: '001'},
            {name: 'IBM', industry: 'giant', size: 10000, location: '002'},
            {name: 'Oracle', industry: 'data', size: 10000, location: '003'}
        ];
        console.log('call me >> [company]')
        const branch = ({code})=>{
            console.log('>>>>' + code);
            return [this.city({code: code})];
        }
        found = comps.find(e=>{ return e.name === employer });
        return {
            name: found.name,
            industry: found.industry,
            size: found.size,
            location: found.location,
            branch: branch            
        };
    },
    job: ({typ, salary}) => {
        const jobs = [
            {name: 'C10', typ: 'Java', status: 'Open', salary: 8000, openDays: 7, employer: 'IBM'},
            {name: 'C10', typ: '.Net', status: 'Closed', salary: 4000, openDays: 3, employer: 'Sony'},
            {name: 'C11', typ: 'Web', status: 'Open', salary: 20000, openDays: 1, employer: 'Oracle'},
            {name: 'C12', typ: 'Python', status: 'Open', salary: 26000, openDays: 2, employer: 'Oracle'}
        ];
        console.log('call me >> [job]:' + typ)     
        found = jobs.filter(e=>{ return e.typ === typ });        
        const c = ()=>{return this.company({employer: "IBM"});}
        return found; 
    },
}

const app = express();

app.use('/graphql', grapqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true
}))

app.listen(3000)
