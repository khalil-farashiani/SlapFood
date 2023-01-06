package store

import (
	"context"
	"github.com/khalil-farashiani/SlapFood/product_microservice/entity"
	"go.mongodb.org/mongo-driver/bson"
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

func (m *MongoDB) GetProduct(ctx context.Context, id int64) (entity.Product, error) {
	var p *Product
	coll := m.Db.Database(productDataBaseName).Collection(productsCollectionName)
	filter := bson.D{{"_id", bson.D{{"$eq", id}}}}
	if err := coll.FindOne(ctx, filter).Decode(p); err != nil {
		return entity.Product{}, err
	}

	return MapProductModelToProductEntity(*p), nil
}
