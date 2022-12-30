package v1

import (
	"io"
	"net/http"
)

func TestHandler(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hello from a test handler!\n")
}
