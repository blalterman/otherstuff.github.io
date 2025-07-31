---
layout: single
title: Publications
permalink: /publications/
---

## Statistics

This page is automatically generated using data from [NASA ADS](https://ui.adsabs.harvard.edu) and is updated weekly.

- **h-index**: {{ site.data.ads_metrics["indicators"]["h"] }}
- **Total number of papers**: {{ site.data.ads_metrics["basic stats"]["number of papers"] }}
- **Total number of citations**: {{ site.data.ads_metrics["citation stats"]["total number of citations"] }}
- **Refereed papers**: {{ site.data.ads_metrics["basic stats refereed"]["number of papers"] }}
- **Refereed citations**: {{ site.data.ads_metrics["citation stats refereed"]["total number of citations"] }}

## Publication List

{% assign pubs_by_type = site.data.ads_publications | group_by: "publication_type" %}
{% assign custom_order = "phdthesis,article,inproceedings,abstract,techreport,eprint" | split: "," %}

{% for type in custom_order %}
{% assign group = pubs_by_type | where: "name", type | first %}
{% if group %}
{% if group.name == "phdthesis" %}

<h2>PhD Thesis</h2>
{% elsif group.name == "article" %}
<h2>Refereed Publications</h2>
{% elsif group.name == "inproceedings" %}
<h2>Conference Proceedings</h2>
{% elsif group.name == "abstract" %}
<h2>Conference Presentations</h2>
{% elsif group.name == "techreport" %}
<h2>White Papers</h2>
{% elsif group.name == "eprint" %}
<h2>Pre-Prints</h2>
{% else %}
<h2>{{ group.name | capitalize }}</h2>
{% endif %}

<div class="publication-table-wrapper">
<table class="publication-table">
  <thead>
    <tr>
      <th>Year</th>
      <th>Title</th>
      <th>Authors</th>
      <th>Journal</th>
      <th>Citations</th>
    </tr>
  </thead>
  <tbody>
    {% assign pubs = group.items | sort: "year" | reverse %}
    {% for pub in pubs %}
      {% include publication_row.liquid pub=pub %}
    {% endfor %}
  </tbody>
</table>
</div>
  {% endif %}
{% endfor %}
