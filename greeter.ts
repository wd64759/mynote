function hello(person: Employee|Person) {
    // return "hello " + person.name + ", age=" + person.age
    return `Hello ${person.name}, who living in the earth for ${person.age} years`
}

interface Person{
    name: string;
    age: number;
}

class Employee {
    name: string;
    age: number;
    company: string;
    constructor(name: string, age: number, company: string) {
        this.name = name
        this.age = age
        this.company = company
    }
}

let James = {
    name: "James Bond",
    age: 45
}

let Jone = new Employee('John Woof', 23, 'holiday inn')
document.body.textContent = hello(James)