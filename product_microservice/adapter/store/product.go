package store

import (
	"context"
	"github.com/khalil-farashiani/SlapFood/product_microservice/entity"
)

const (
	productDataBaseName    = "product_service"
	productsCollectionName = "products"
)

func (m *MongoDB) CreateProduct(ctx context.Context, p entity.Product) (entity.Product, error) {
	pModel := MapProductEntityToProductModel(p)
	coll := m.Db.Database(productDataBaseName).Collection(productsCollectionName)
	if _, err := coll.InsertOne(ctx, pModel); err != nil {
		return entity.Product{}, err
	}
	return MapProductModelToProductEntity(pModel), nil
}
