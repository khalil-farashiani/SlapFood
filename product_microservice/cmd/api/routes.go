package main

import (
	"net/http"
	"log"
	"github.com/gorilla/mux"
)

func routes() http.Handler{
	log.Println(
		"start server on port 8080",
	)
	r := mux.NewRouter()	
	return r

}