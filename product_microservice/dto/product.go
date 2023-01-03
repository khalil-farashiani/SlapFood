package dto

import (
	"github.com/khalil-farashiani/SlapFood/product_microservice/entity"
	"time"
)

type CreateProductRequest struct {
	Name        string   `json:"name"`
	Description string   `json:"description"`
	Price       int64    `json:"price"`
	Category    string   `json:"category"`
	Features    []string `json:"features"`
}

type CreateProductResponse struct {
	ID          string    `json:"id"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
	Name        string    `json:"name"`
	Description string    `json:"description"`
	Price       int64     `json:"price"`
	Category    string    `json:"category"`
	Features    []string  `json:"features"`
}

type GetProductResponse struct {
	Product entity.Product `json:"product"`
}

type UpdateProductRequest struct {
	Name        string   `json:"name"`
	Description string   `json:"description"`
	Price       int64    `json:"price"`
	Category    string   `json:"category"`
	Features    []string `json:"features"`
}

type UpdateProductResponse struct {
	Product entity.Product
}

type FindProductsRequest struct {
	Id int64 `json:"id"`
}

type FindProductsResponse struct {
	Products []entity.Product `json:"products"`
}

type FindProductRequest struct {
	Id int64 `json:"id"`
}

type FindProductResponse struct {
	Product entity.Product `json:"product"`
}

type DeleteProductRequest struct {
	Id int64 `json:"id"`
}

type DeleteProductResponse struct {
	Message string `json:"message"`
}
