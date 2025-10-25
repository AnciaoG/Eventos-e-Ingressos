const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export async function apiGet(path) {
  try {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) {
      throw new Error(`API GET ${path} falhou (${res.status})`);
    }
    return res.json();
  } catch (error) {
    console.error('Erro em apiGet:', error);
    throw error;
  }
}

export async function apiPost(path, body) {
  try {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json' 
      },
      body: JSON.stringify(body)
    });
    
    if (!res.ok) {
      const text = await res.text();
      throw new Error(`API POST ${path} falhou (${res.status}): ${text}`);
    }
    
    return res.json();
  } catch (error) {
    console.error('Erro em apiPost:', error);
    throw error;
  }
}
