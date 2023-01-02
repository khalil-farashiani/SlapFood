package store

import (
	"github.com/google/uuid"
	"github.com/khalil-farashiani/SlapFood/product_microservice/entity"
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

func MapProductModelToProductEntity(p Product) entity.Product {
	return entity.Product{
		ID:          p.ID.String(),
		CreatedAt:   p.CreatedAt,
		UpdatedAt:   p.UpdatedAt,
		Name:        p.Name,
		Description: p.Description,
		Price:       p.Price,
		Category:    p.Category,
		Features:    p.Features,
	}
}

func MapProductEntityToProductModel(p entity.Product) Product {
	return Product{
		CreatedAt:   p.CreatedAt,
		UpdatedAt:   p.UpdatedAt,
		Name:        p.Name,
		Description: p.Description,
		Price:       p.Price,
		Category:    p.Category,
		Features:    p.Features,
	}
}
