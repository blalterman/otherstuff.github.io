---
layout: single
title: Publications
permalink: /publications/
---

This page is automatically generated using data from [NASA ADS](https://ui.adsabs.harvard.edu) and is updated weekly.

- **h-index**: {{ site.data.ads_metrics["indicators"]["h"] }}
- **Total number of papers**: {{ site.data.ads_metrics["basic stats"]["number of papers"] }}
- **Total number of citations**: {{ site.data.ads_metrics["citation stats"]["total number of citations"] }}
- **Refereed papers**: {{ site.data.ads_metrics["basic stats refereed"]["number of papers"] }}
- **Refereed citations**: {{ site.data.ads_metrics["citation stats refereed"]["total number of citations"] }}


## Publications

<ul class="publication-list">
{% assign pubs = site.data.ads_publications | sort: "year" | reverse %}
{% for pub in pubs %}
  {% assign formatted_authors = "" %}
  {% for author in pub.authors %}
    {% if author contains "Alterman" %}
      {% assign author = author | replace: "Ben Alterman", "<strong>Ben Alterman</strong>" %}
      {% assign author = author | replace: "Benjamin Alterman", "<strong>Benjamin Alterman</strong>" %}
      {% assign author = author | replace: "Benjamin L. Alterman", "<strong>Benjamin L. Alterman</strong>" %}
      {% assign author = author | replace: "B. Alterman", "<strong>B. Alterman</strong>" %}
      {% assign author = author | replace: "B. L. Alterman", "<strong>B. L. Alterman</strong>" %}
      {% assign author = author | replace: "Alterman, B.", "<strong>Alterman, B.</strong>" %}
      {% assign author = author | replace: "Alterman, B. L.", "<strong>Alterman, B. L.</strong>" %}
    {% endif %}
    {% assign formatted_authors = formatted_authors | append: author %}
    {% unless forloop.last %}
      {% assign formatted_authors = formatted_authors | append: ", " %}
    {% endunless %}
  {% endfor %}
  <li>
    <strong><a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a></strong><br>
    <span class="authors">{{ formatted_authors }}</span><br>
    <em>{{ pub.journal }}</em>, {{ pub.year }}.
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

