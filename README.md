# elmnthealth-verify (temporary)

Serves `https://elmnthealth.com/merchantcenter.txt` for Google Merchant Center
account recovery (case 5-7807000042170, accounts 705765203 / 5470648282).
The homepage stays on elmnthealth.com and offers a link to the store.
Unknown paths forward visitors to terraelmnt.com through the custom 404 page.

While this is live, elmnthealth.com's root A records point at GitHub Pages
instead of Shopify. Once Google confirms, restore Shopify's records
(A `@` 23.227.38.73, AAAA `@` 2620:127:f00f:d::), then delete this repo.

To retest after a hosting or DNS change, run **Check public verification URLs**
from the Actions tab. It checks HTTPS status, content type, deployed contents,
and the final address of both URLs in a fresh incognito Chrome session.
