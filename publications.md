---
layout: single
title: Publications
permalink: /publications/
---

## Publications

This page is automatically generated using citation data from [NASA ADS](https://ui.adsabs.harvard.edu).

- **h-index**: {{ site.data.ads_metrics["indicators"]["h"] }}
- **Total number of papers**: {{ site.data.ads_metrics["basic stats"]["number of papers"] }}
- **Total number of citations**: {{ site.data.ads_metrics["citation stats"]["total number of citations"] }}
- **Refereed papers**: {{ site.data.ads_metrics["basic stats refereed"]["number of papers"] }}
- **Refereed citations**: {{ site.data.ads_metrics["citation stats refereed"]["total number of citations"] }}

## Pretty table


<style>
  .metrics-table {
    width: 100%;
    max-width: 600px;
    margin-top: 1em;
    border-collapse: collapse;
    font-size: 1rem;
  }
  .metrics-table th,
  .metrics-table td {
    border: 1px solid #ccc;
    padding: 0.6em 1em;
    text-align: left;
  }
  .metrics-table th {
    background-color: #f8f8f8;
    font-weight: 600;
  }
  .metrics-table caption {
    text-align: left;
    font-size: 1.25em;
    font-weight: bold;
    padding: 0.5em 0;
  }
</style>

<table class="metrics-table">
  <caption>Citation Metrics</caption>
  <tbody>
    <tr>
      <th>Total papers</th>
      <td>{{ site.data.ads_metrics["basic stats"]["number of papers"] }}</td>
    </tr>
    <tr>
      <th>Refereed papers</th>
      <td>{{ site.data.ads_metrics["basic stats refereed"]["number of papers"] }}</td>
    </tr>
    <tr>
      <th>Total citations</th>
      <td>{{ site.data.ads_metrics["citation stats"]["total number of citations"] }}</td>
    </tr>
    <tr>
      <th>Refereed citations</th>
      <td>{{ site.data.ads_metrics["citation stats refereed"]["total number of citations"] }}</td>
    </tr>
    <tr>
      <th>h-index</th>
      <td>{{ site.data.ads_metrics["indicators"]["h"] }}</td>
    </tr>
  </tbody>
</table>



## Publication List

---
layout: page
title: My Publications
permalink: /publications/
---

This list of publications is automatically updated weekly using data from [NASA ADS](https://ui.adsabs.harvard.edu).

<table class="pub-table">
  <thead>
    <tr>
      <th>Title</th>
      <th>Authors</th>
      <th>Journal</th>
      <th>Date</th>
      <th>Citations</th>
    </tr>
  </thead>
  <tbody>
  {% assign pubs = site.data.ads_publications | sort: "year" | reverse %}
  {% for pub in pubs %}
    <tr>
      <td>
        <a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a>
      </td>
      <td>{{ pub.authors | join: ", " }}</td>
      <td>{{ pub.journal }}</td>
      <td>{{ pub.month }} {{ pub.year }}</td>
      <td>{{ pub.citations }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<style>
  .pub-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1em;
    font-size: 0.95rem;
  }
  .pub-table th,
  .pub-table td {
    border: 1px solid #ccc;
    padding: 0.6em;
    text-align: left;
  }
  .pub-table th {
    background-color: #f0f0f0;
    font-weight: bold;
  }
  .pub-table a {
    color: #0645ad;
    text-decoration: none;
  }
  .pub-table a:hover {
    text-decoration: underline;
  }
</style>
