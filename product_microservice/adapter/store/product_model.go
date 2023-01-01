package store

import (
	"github.com/google/uuid"
	"time"
)

type Product struct {
	ID          uuid.UUID `bson:"_id"`
	CreatedAt   time.Time `bson:"created_at"`
	UpdatedAt   time.Time `bson:"updated_at"`
	Name        string    `bson:"name"`
	Description string    `bson:"description"`
	Price       int64     `bson:"price"`
	Category    string    `bson:"category"`
	Features    []string  `bson:"features"`
}
