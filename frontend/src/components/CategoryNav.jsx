import './CategoryNav.css';

const categories = [
  'All',
  'Electronics',
  'Fashion',
  'Accesories',
  'Kids',
  'Furniture',
  'Groceries',
  'Kitchenwares',
];

function CategoryNav() {
  return (
    <nav className="category-nav">
      {categories.map((cat, idx) => (
        <span key={cat} className={`category-tab${idx === 0 ? ' active' : ''}`}>{cat}</span>
      ))}
    </nav>
  );
}

export default CategoryNav; 