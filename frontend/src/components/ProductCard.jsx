import './ProductCard.css';

function ProductCard({ image, name, rating, price }) {
  return (
    <div className="product-card">
      <img src={image} alt={name} className="product-img" />
      <div className="product-info">
        <div className="product-name">{name}</div>
        <div className="product-rating">
          {Array.from({ length: 5 }).map((_, i) => (
            <span key={i} className={i < Math.floor(rating) ? 'star filled' : 'star'}>★</span>
          ))}
          <span className="rating-value">{rating}/5</span>
        </div>
        <div className="product-price">${price}</div>
      </div>
    </div>
  );
}

export default ProductCard; 