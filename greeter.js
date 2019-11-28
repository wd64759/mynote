function hello(person) {
    // return "hello " + person.name + ", age=" + person.age
    return "Hello " + person.name + ", who living in the earth for " + person.age + " years";
}
var Employee = /** @class */ (function () {
    function Employee(name, age, company) {
        this.name = name;
        this.age = age;
        this.company = company;
    }
    return Employee;
}());
var James = {
    name: "James Bond",
    age: 45
};
var Jone = new Employee('John Woof', 23, 'holiday inn');
document.body.textContent = hello(James);
