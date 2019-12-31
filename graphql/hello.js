// Function: possible to reduce sub query based on reflesion

const express = require('express')
const  {buildSchema} = require('graphql')
const grapqlHTTP = require('express-graphql')

const schema = buildSchema(`
    type Query {
        job(typ: String, salary: Int): [Job],
        city(code: String!): City,
        company(employer: String!, loc_code: String): Company
    },
    type Job {
        name: String,
        typ: String,
        status: String,
        salary: Int,
        openDays: Int,
        employer: String,
        location: String,
        company(employer: String): Company,
        city(code: String): City
    },
    type Company {
        name: String,
        industry: String,
        size: Int,
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
        console.log('call [city] >> ' + code)
        const cities = [
            {'name': 'xian', 'state': 'Shan Xi', 'population': 6000000, 'code': '002'},
            {'name': 'shanghai', 'state': 'Shang Hai', 'population': 30000000, 'code': '001'},
            {'name': 'chengdu', 'state': 'Si Chuan', 'population': 4000000, 'code': '003'}
        ];
        const found = cities.find(e=>{ return e.code === code });
        return found;
    },
    company({employer, loc_code}) {
        console.log('call [company] >> ' + employer)
        const comps = [
            {name: 'Sony', industry: 'media', size: 10000, city_codes: ["002", "003"]},
            {name: 'IBM', industry: 'giant', size: 10000, city_codes: ["001", "003"]},
            {name: 'Oracle', industry: 'data', size: 10000, city_codes: ["001", "002"]}
        ];
        const found = comps.find(e=>{ return e.name === employer });
        const branch = ({code})=>{
            let cities = []            
            if(code) {
                cities.push(this.city({code: code}))
            } else {
                if (found && loc_code) {
                    found.city_codes = found.city_codes.filter(e=>e === loc_code)
                }
                if (found && found.city_codes) {            
                    for (let e of found.city_codes) {
                        cities.push(this.city({code: e}));
                    }
                }        
            }
            return cities;
        }
        found["branch"] = branch        
        return {
            name: found.name,
            industry: found.industry,
            size: found.size,
            branch: found.branch            
        };
    },
    job({typ, salary}) {
        console.log('call [job] >> ' + typ)
        const jobs = [
            {name: 'C10', typ: 'Java', status: 'Open', salary: 8000, openDays: 7, employer: 'IBM', location: '001'},
            {name: 'C10', typ: '.Net', status: 'Closed', salary: 4000, openDays: 3, employer: 'Sony', location: '002'},
            {name: 'C11', typ: 'Java', status: 'Open', salary: 20000, openDays: 1, employer: 'Oracle', location: '002'},
            {name: 'C12', typ: 'Python', status: 'Open', salary: 26000, openDays: 2, employer: 'Oracle', location: '003'}
        ];
        const found = typ?jobs.filter(e=>{ return e.typ === typ }):jobs;
        if (found) {
            for (let job of found) {
                const com = this.company({employer: job.employer, loc_code: job.location});
                job.company = com;
                const city = this.city({code: job.location});
                job.city = city;                   
            }
        }        
        return found; 
    },
}

const app = express();

app.use('/graphql', grapqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true
}))

app.use(express.static('public'))

app.listen(3000)
