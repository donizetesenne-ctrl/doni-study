// Service Worker — permite instalar como app e cache offline
const CACHE_NAME = 'doni-study-v1';
const ASSETS = [
    './',
    './index.html',
    './manifest.json'
];

// Instalar — cachear arquivos base
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
    );
    self.skipWaiting();
});

// Ativar — limpar caches antigos
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => 
            Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
        )
    );
    self.clients.claim();
});

// Fetch — cache first, then network
self.addEventListener('fetch', event => {
    // Não cachear chamadas de API
    if (event.request.url.includes('googleapis.com')) {
        return;
    }

    event.respondWith(
        caches.match(event.request).then(cached => {
            return cached || fetch(event.request).then(response => {
                // Cachear nova resposta
                if (response.status === 200) {
                    const clone = response.clone();
                    caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
                }
                return response;
            });
        }).catch(() => {
            // Offline fallback
            return caches.match('./index.html');
        })
    );
});
