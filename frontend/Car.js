// Конструктор, формирующий поля класс по объекту JSON
function Car(obj) {
    this.id = obj.id;
    this.full_name = obj.full_name;
    this.phone_number = obj.phone_number;
}

// Реализация класса 
Car.prototype = {
    constructor: Car,
    print: function(){
        console.log(this.to_string());
    },
    to_string: function() {
        return "Id: " + this.id + ", full_name: " + this.full_name + ", phone_number: " + this.phone_number;
    },
    // Используемый ранее метод, возвращающий форматированные поля класса
    // <tr>...</tr> - строка таблиы, table row
    // <td>...</td> - элемент на пересечении колонки и строки
    to_table_entry: function() {
        return '<tr><td>' + 
        this.id + '</td><td>' + 
        this.full_name + '</td><td>' + 
        this.phone_number + '</td></tr>'
    }
}