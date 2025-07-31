---
layout: single
title: Publications
permalink: /publications/
---

## Publications

This page is automatically generated using citation data from [NASA ADS](https://ui.adsabs.harvard.edu).

- **h-index**: {{ site.data.ads_metrics["citation stats"]["h index"] }}
- **Total number of papers**: {{ site.data.ads_metrics["citation stats"]["total number of papers"] }}
- **Total number of citations**: {{ site.data.ads_metrics["citation stats"]["total number of citations"] }}
- **Refereed papers**: {{ site.data.ads_metrics["citation stats"]["number of refereed papers"] }}
- **Refereed citations**: {{ site.data.ads_metrics["citation stats"]["number of refereed citations"] }}

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
      <td>{{ site.data.ads_metrics["citation stats"]["total number of papers"] }}</td>
    </tr>
    <tr>
      <th>Refereed papers</th>
      <td>{{ site.data.ads_metrics["citation stats"]["number of refereed papers"] }}</td>
    </tr>
    <tr>
      <th>Total citations</th>
      <td>{{ site.data.ads_metrics["citation stats"]["total number of citations"] }}</td>
    </tr>
    <tr>
      <th>Refereed citations</th>
      <td>{{ site.data.ads_metrics["citation stats"]["number of refereed citations"] }}</td>
    </tr>
    <tr>
      <th>h-index</th>
      <td>{{ site.data.ads_metrics["citation stats"]["h index"] }}</td>
    </tr>
  </tbody>
</table>