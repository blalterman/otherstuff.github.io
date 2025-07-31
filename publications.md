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
  .stats-table {
    border-collapse: collapse;
    width: 100%;
    max-width: 600px;
    margin-top: 1em;
  }
  .stats-table th,
  .stats-table td {
    border: 1px solid #ddd;
    padding: 0.6em;
    text-align: left;
  }
  .stats-table th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  .stats-table caption {
    caption-side: top;
    font-size: 1.2em;
    font-weight: bold;
    margin-bottom: 0.5em;
    text-align: left;
  }
</style>

<table class="stats-table">
  <caption>ADS Citation Metrics</caption>
  <tbody>
    <tr><th>Total papers</th><td>{{ site.data.ads_metrics["citation stats"]["total number of papers"] }}</td></tr>
    <tr><th>Refereed papers</th><td>{{ site.data.ads_metrics["citation stats"]["number of refereed papers"] }}</td></tr>
    <tr><th>Total citations</th><td>{{ site.data.ads_metrics["citation stats"]["total number of citations"] }}</td></tr>
    <tr><th>Refereed citations</th><td>{{ site.data.ads_metrics["citation stats"]["number of refereed citations"] }}</td></tr>
    <tr><th>h-index</th><td>{{ site.data.ads_metrics["citation stats"]["h index"] }}</td></tr>
    <tr><th>Normalized h-index</th><td>{{ site.data.ads_metrics["citation stats"]["normalized h index"] }}</td></tr>
    <tr><th>i10 index</th><td>{{ site.data.ads_metrics["citation stats"]["i10 index"] }}</td></tr>
    <tr><th>tori index</th><td>{{ site.data.ads_metrics["citation stats"]["tori index"] }}</td></tr>
    <tr><th>riq index</th><td>{{ site.data.ads_metrics["citation stats"]["riq index"] }}</td></tr>
  </tbody>
</table>