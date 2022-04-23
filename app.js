const express =  require ("express");
const mysql = require("mysql");
const path = require("path");
const res = require("express/lib/response");
const cookieParser= require("cookie-parser");

const app= express();
const dotenv= require('dotenv');
dotenv.config({path: './.env'});
const db = mysql.createConnection({
    host: process.env.DATABASE_HOST,
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASS,
    database: process.env.DATABASE, 


});
const publicDirectory = path.join(__dirname,'./public');
console.log(__dirname);

app.use(express.static(publicDirectory));

//parse url encoded bodies
app.use(express.urlencoded({extended: false}))
app.use(express.json())
app.use(cookieParser());

app.set('view engine','hbs');
db.connect((error)=>{
    if(error){
        console.log(error)
    }
    else{
        console.log("Mysql connected..")
    }
})



//Define routes
app.use('/',require('./routes/pages'))
app.use('/auth',require('./routes/auth'))

app.listen(5000,()=>{
    console.log("Server started on port 5000")
})
