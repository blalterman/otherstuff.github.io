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



## Publication List

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



## Responsive table

<div class="table-responsive">
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
        <td><a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a></td>
        <td>{{ pub.authors | join: ", " }}</td>
        <td>{{ pub.journal }}</td>
        <td>{{ pub.month }} {{ pub.year }}</td>
        <td>{{ pub.citations }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<style>
  .table-responsive {
    width: 100%;
    overflow-x: auto;
  }
  .pub-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
  }
  .pub-table th,
  .pub-table td {
    border: 1px solid #ccc;
    padding: 0.6em;
    text-align: left;
    white-space: nowrap;
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
