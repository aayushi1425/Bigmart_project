import ProductCard from './ProductCard';
import products from '../data/products.json';
import './ProductList.css';

function repeatProducts(arr, minCount) {
  const repeated = [];
  while (repeated.length < minCount) {
    repeated.push(...arr);
  }
  return repeated.slice(0, minCount);
}

function ProductList() {
  // Assume 4 cards per row on desktop, so fill at least 8 cards per section
  const mainProducts = repeatProducts(products, 8);
  const topSelling = repeatProducts(products.slice(4, 8), 8);

  return (
    <section className="product-list-section">
      <div className="product-grid">
        {mainProducts.map((product, idx) => (
          <ProductCard key={product.id + '-main-' + idx} {...product} />
        ))}
      </div>
      <div className="explore-btn-wrap">
        <button className="explore-btn">Explore all items</button>
      </div>
      <h2 className="top-selling-title">Top Selling Products</h2>
      <div className="product-grid">
        {topSelling.map((product, idx) => (
          <ProductCard key={product.id + '-top-' + idx} {...product} />
        ))}
      </div>
      <div className="explore-btn-wrap">
        <button className="explore-btn">Explore all items</button>
      </div>
    </section>
  );
}

export default ProductList; 