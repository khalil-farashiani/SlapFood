package main

import (
	"context"
	"flag"
	"github.com/khalil-farashiani/SlapFood/product_microservice/adapter/store"
	"log"
	"net/http"
	"os"
	"os/signal"
	"time"
)

const (
	durationMessage = "the duration for which the server gracefully wait for existing connections to finish - e.g. 15s or 1m"
	gracfullMessage = "graceful-timeout"
	servAddress     = "127.0.0.1:8080"
)

func main() {

	var wait time.Duration
	flag.DurationVar(&wait, gracfullMessage, time.Second*15, durationMessage)
	flag.Parse()

	r := routes()

	srv := &http.Server{
		Addr:         servAddress,
		WriteTimeout: time.Second * 15,
		ReadTimeout:  time.Second * 15,
		IdleTimeout:  time.Second * 60,
		Handler:      r, // Pass our instance of gorilla/mux in.
	}

	// Run our server in a goroutine so that it doesn't block.
	go func() {
		if err := srv.ListenAndServe(); err != nil {
			log.Panic(err)
		}
	}()

	mongo := store.InitMongo()
	defer mongo.Disconnect(context.Background())

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)
	<-c

	ctx, cancel := context.WithTimeout(context.Background(), wait)
	defer cancel()

	srv.Shutdown(ctx)

	log.Println("shutting down")
	os.Exit(0)
}
