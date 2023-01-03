package contract

import (
	"context"
	"github.com/khalil-farashiani/SlapFood/product_microservice/dto"
)

type ProductIntractor interface {
	CreateProduct(context.Context, dto.CreateProductRequest) (dto.CreateProductResponse, error)
	UpdateProduct(context.Context, dto.UpdateProductRequest) (dto.UpdateProductResponse, error)
	FindProducts(context.Context, dto.FindProductsRequest) (dto.FindProductRequest, error)
	FindProduct(context.Context, dto.FindProductsRequest) (dto.FindProductResponse, error)
	DeleteProduct(context.Context, dto.DeleteProductRequest) (dto.DeleteProductResponse, error)
}
