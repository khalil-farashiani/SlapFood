package main

import (
	v1 "github.com/khalil-farashiani/SlapFood/product_microservice/delivery/http/v1"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func routes() http.Handler {
	log.Println(
		"start server on port 8080",
	)
	r := mux.NewRouter()

	r.HandleFunc("/", v1.TestHandler).Methods("GET")
	return r

}
