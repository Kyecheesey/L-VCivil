# Domain transfer & DNS cutover — lvcivilcontracting.com.au

The previous provider has cancelled the `lvcivilcontracting.com.au` service and issued
the domain's EPP (transfer authorisation) code plus a snapshot of the live DNS records
(email to director@kwinnovations.com.au, 30 Jul 2026). This is the runbook for moving
the domain to our registrar and cutting DNS over to the new site in this repo.

> **EPP code:** deliberately **not** stored in this repo — it authorises transferring
> the domain away, so it must never sit in git history. It's in the 30 Jul 2026
> cancellation email; keep it in the KW Innovations password manager until the
> transfer completes, then it's void (a new code is issued by the gaining registrar).

## Current DNS snapshot (pre-transfer)

Everything below points at the **old Duda-hosted site** (`s.multiscreensite.com` is
Duda; the A records are its AWS front-ends). Zone is served by AWS Route 53.

| Record | TTL | Type | Value |
|---|---|---|---|
| `lvcivilcontracting.com.au.` | 600 | A | `100.24.208.97` |
| `lvcivilcontracting.com.au.` | 600 | A | `35.172.94.1` |
| `lvcivilcontracting.com.au.` | 600 | TXT | `"google-site-verification=c0C4uAcPlO4BwAWsR2lgP9D5e6XOIEhlebp1gIzbEK4"` |
| `lvcivilcontracting.com.au.` | 600 | NS | `ns-1241.awsdns-27.org.` |
| `lvcivilcontracting.com.au.` | 600 | NS | `ns-1612.awsdns-09.co.uk.` |
| `lvcivilcontracting.com.au.` | 600 | NS | `ns-452.awsdns-56.com.` |
| `lvcivilcontracting.com.au.` | 600 | NS | `ns-982.awsdns-58.net.` |
| `www.lvcivilcontracting.com.au.` | 600 | CNAME | `s.multiscreensite.com.` |

**Note — no MX records in the snapshot.** `info@lvcivilcontracting.com.au` (the
enquiry address baked into `build.py` and `js/main.js`) either has mail hosted with
records not included in this dump, or has no working mailbox. **Verify before
cutover** — `dig MX lvcivilcontracting.com.au` while the old zone is still live, and
replicate any MX/SPF/DKIM records in the new zone, or stand up mail (e.g. Google
Workspace / Microsoft 365) if none exist. Losing the enquiry inbox is the biggest
cutover risk.

## Transfer steps (.au domain)

1. **Before the old service is switched off**, capture anything missing from the
   snapshot: `dig MX`, `dig TXT` (SPF/DMARC), and any subdomains in use.
2. Confirm the registrant contact is correct — .au transfers require the registrant
   (or authorised contact) to approve, and eligibility (ABN — it's in the site
   footer) carries over.
3. Initiate the transfer at our registrar using the EPP code from the email.
   .au transfers are free at most registrars, don't change the expiry date, and
   usually complete within hours once approved.
4. Approve the confirmation email sent to the registrant contact.
5. Once transferred, the domain will initially keep the AWS Route 53 name servers
   above. **Don't touch DNS until the new site is deployed** — the old site keeps
   working in the meantime only if the old zone stays up; if the provider tears the
   Route 53 zone down, move to our own DNS immediately (recreate the snapshot
   records) even before the new site is ready.

## DNS cutover to the new site

When the new build (this repo) is deployed to its host:

1. Point name servers (or just the A/CNAME records if we recreate the zone) at the
   new host — e.g. Cloudflare Pages / Netlify / Vercel per the README. Remove the
   two Duda A records and the `www` → `s.multiscreensite.com` CNAME.
2. **Keep the `google-site-verification` TXT record** — it preserves Search Console
   ownership. Add a second verification (DNS record from our own Search Console
   account) rather than replacing it.
3. Recreate MX/SPF/DKIM/DMARC as found in step 1 above.
4. Serve `www` → apex redirect (or vice-versa, matching whichever the old site
   canonicalised to) so existing links and rankings carry over.
5. TTLs are already 600s, so propagation is quick; verify with
   `dig +short lvcivilcontracting.com.au` and a crawl of the URLs in `sitemap.xml`
   (paths intentionally match the old site 1:1 — see README).
6. After cutover, submit `sitemap.xml` in Search Console and monitor coverage.
