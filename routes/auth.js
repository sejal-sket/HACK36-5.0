const { Router } = require("express");
const express= require("express");
const authController =require('../controllers/auth')
const { route } = require("express/lib/application");
const router= express.Router();
router.post('/register' ,authController.register);
router.post('/login' ,authController.login);
router.post('/book' ,authController.book);
router.get('/logout',authController.logout)

module.exports=router;
