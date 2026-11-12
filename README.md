# elmnthealth-verify (temporary)

Serves `https://elmnthealth.com/merchantcenter.txt` for Google Merchant Center
account recovery (case 5-7807000042170, accounts 705765203 / 5470648282).
Every other path forwards to terraelmnt.com.

While this is live, elmnthealth.com's root A records point at GitHub Pages
instead of Shopify. Once Google confirms, restore Shopify's records
(A `@` 23.227.38.73, AAAA `@` 2620:127:f00f:d::), then delete this repo.
