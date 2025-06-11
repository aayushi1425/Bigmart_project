import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const productService = {
  getAll: async () => {
    try {
      const response = await api.get('/products');
      return response.data;
    } catch (error) {
      console.error('Error fetching products:', error);
      throw error;
    }
  },

  getById: async (id) => {
    try {
      const response = await api.get(`/products/${id}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching product ${id}:`, error);
      throw error;
    }
  },

  create: async (product) => {
    try {
      const response = await api.post('/products', product);
      return response.data;
    } catch (error) {
      console.error('Error creating product:', error);
      throw error;
    }
  },

  update: async (id, product) => {
    try {
      const response = await api.put(`/products/${id}`, product);
      return response.data;
    } catch (error) {
      console.error(`Error updating product ${id}:`, error);
      throw error;
    }
  },

  delete: async (id) => {
    try {
      await api.delete(`/products/${id}`);
    } catch (error) {
      console.error(`Error deleting product ${id}:`, error);
      throw error;
    }
  }
}; 