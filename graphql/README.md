### Data Domain Service
``` js
query {
  job(typ: "Java") {
    name,
    typ,
    status,
    openDays,
    employer
  }
  company(employer: "IBM") {
    name,
    industry,
    size,
    location
  }
  city(code: "001") {
    name,
    state,
    population    
  }
}
```