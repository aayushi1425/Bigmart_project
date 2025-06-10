import Navbar from './components/Navbar';
import Hero from './components/Hero';
import CategoryNav from './components/CategoryNav';
import ProductList from './components/ProductList';
import Newsletter from './components/Newsletter';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="bigmart-root">
      <Navbar />
      <Hero />
      <CategoryNav />
      <ProductList />
      <Newsletter />
      <Footer />
    </div>
  );
}

export default App;
