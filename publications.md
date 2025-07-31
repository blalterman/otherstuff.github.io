---
layout: single
title: Publications
permalink: /publications/
---

## Publications

This page is automatically generated using data from [NASA ADS](https://ui.adsabs.harvard.edu) and is updated weekly.

- **h-index**: {{ site.data.ads_metrics["indicators"]["h"] }}
- **Total number of papers**: {{ site.data.ads_metrics["basic stats"]["number of papers"] }}
- **Total number of citations**: {{ site.data.ads_metrics["citation stats"]["total number of citations"] }}
- **Refereed papers**: {{ site.data.ads_metrics["basic stats refereed"]["number of papers"] }}
- **Refereed citations**: {{ site.data.ads_metrics["citation stats refereed"]["total number of citations"] }}


## Publications

{% assign pubs = site.data.ads_publications | sort: "year" | reverse %}
{% for pub in pubs %}
  <li>
    <strong><a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a></strong><br>
    <span class="authors">{{ pub.authors | join: ", " }}</span><br>
    <span class="journal">{{ pub.journal }}</span>,
    <span class="date">{{ pub.month }} {{ pub.year }}</span>.
    <span class="citations">Citations: {{ pub.citations }}</span>
  </li>
{% endfor %}
</ul>

<style>
.publication-list {
  list-style-type: disc;
  padding-left: 1.5em;
}
.publication-list li {
  margin-bottom: 1.2em;
  line-height: 1.5em;
}
.publication-list a {
  text-decoration: none;
  color: #0645ad;
}
.publication-list a:hover {
  text-decoration: underline;
}
</style>