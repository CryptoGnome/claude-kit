# JSON-LD snippets

Copy-paste `<script type="application/ld+json">` templates for the `seo-geo-aeo` skill. Fill the placeholders, then validate at validator.schema.org and Google's Rich Results Test.

## Organization — GEO entity clarity (put on the homepage)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "...",
  "url": "https://...",
  "logo": "https://.../logo.png",
  "sameAs": [
    "https://twitter.com/...",
    "https://github.com/...",
    "https://www.linkedin.com/company/..."
  ]
}
```

## Article — with author for E-E-A-T
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "datePublished": "2026-01-01",
  "dateModified": "2026-01-01",
  "author": { "@type": "Person", "name": "...", "url": "https://.../about" },
  "publisher": {
    "@type": "Organization",
    "name": "...",
    "logo": { "@type": "ImageObject", "url": "https://.../logo.png" }
  }
}
```

## FAQPage — AEO answer boxes
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "...?",
      "acceptedAnswer": { "@type": "Answer", "text": "..." }
    }
  ]
}
```

## HowTo — AEO step snippets
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "...",
  "step": [
    { "@type": "HowToStep", "name": "...", "text": "..." }
  ]
}
```

## BreadcrumbList — SEO navigation context
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://..." },
    { "@type": "ListItem", "position": 2, "name": "...", "item": "https://.../..." }
  ]
}
```

## Product — e-commerce rich results
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "...",
  "image": "https://.../product.png",
  "description": "...",
  "brand": { "@type": "Brand", "name": "..." },
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://..."
  },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "128" }
}
```

## LocalBusiness — local pack + AEO
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "...",
  "url": "https://...",
  "telephone": "+1-555-000-0000",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "...",
    "addressLocality": "...",
    "addressRegion": "..",
    "postalCode": "...",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "..", "longitude": ".." },
  "openingHours": "Mo-Fr 09:00-17:00"
}
```
