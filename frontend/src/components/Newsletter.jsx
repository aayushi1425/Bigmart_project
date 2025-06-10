import './Newsletter.css';

function Newsletter() {
  return (
    <section className="newsletter-section">
      <div className="newsletter-content">
        <h3>STAY UPTO DATE ABOUT<br />OUR LATEST OFFERS</h3>
        <form className="newsletter-form">
          <input type="email" placeholder="Enter your email address" />
          <button type="submit">Subscribe to Newsletter</button>
        </form>
      </div>
    </section>
  );
}

export default Newsletter; 