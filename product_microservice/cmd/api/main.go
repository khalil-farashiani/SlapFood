package main


import (
	"context"
    "flag"
    "log"
    "net/http"
    "os"
    "os/signal"
    "time"
)

func main() {

	var wait time.Duration
    flag.DurationVar(&wait, "graceful-timeout", time.Second * 15, "the duration for which the server gracefully wait for existing connections to finish - e.g. 15s or 1m")
    flag.Parse()

	r := routes()

	srv := &http.Server{
        Addr:         "127.0.0.1:8080",
        WriteTimeout: time.Second * 15,
        ReadTimeout:  time.Second * 15,
        IdleTimeout:  time.Second * 60,
        Handler: r, // Pass our instance of gorilla/mux in.
    }

    // Run our server in a goroutine so that it doesn't block.
    go func() {
        if err := srv.ListenAndServe(); err != nil {
            log.Panic(err)
        }
    }()

    c := make(chan os.Signal, 1)
    signal.Notify(c, os.Interrupt)
    <-c

    ctx, cancel := context.WithTimeout(context.Background(), wait)
    defer cancel()
  
    srv.Shutdown(ctx)
    
    log.Println("shutting down")
    os.Exit(0)
}