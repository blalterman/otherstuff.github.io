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
{% assign presentations = "" | split: "" %}
{% assign proceedings = "" | split: "" %}
{% assign other_groups = "" | split: "" %}

{% for group in pubs_by_type %}
  {% if group.name == "abstract" %}
    {% assign presentations = group.items %}
  {% elsif group.name == "inproceedings" %}
    {% assign proceedings = group.items %}
  {% else %}
    {% assign other_groups = other_groups | push: group %}
  {% endif %}
{% endfor %}

{% assign sorted_other_groups = other_groups | sort: "name" %}

<h2>Conference Presentations</h2>
<ul class="publication-list">
  {% assign presentations_sorted = presentations | sort: "year" | reverse %}
  {% for pub in presentations_sorted %}
    {% include publication_entry.liquid pub=pub %}
  {% endfor %}
</ul>

<h2>Conference Proceedings</h2>
<ul class="publication-list">
  {% assign proceedings_sorted = proceedings | sort: "year" | reverse %}
  {% for pub in proceedings_sorted %}
    {% include publication_entry.liquid pub=pub %}
  {% endfor %}
</ul>

{% for group in sorted_other_groups %}
{% if group.name == "article" %}
<h2>Refereed Publications</h2>
{% elsif group.name == "techreport" %}
<h2>White Papers</h2>
{% elsif group.name == "eprint" %}
<h2>Pre-Prints</h2>
{% elsif group.name == "phdthesis" %}
<h2>PhD Thesis</h2>
{% else %}
<h2>{{ group.name | capitalize }}</h2>
{% endif %}

  <ul class="publication-list">
    {% assign pubs = group.items | sort: "year" | reverse %}
    {% for pub in pubs %}
      {% include publication_entry.liquid pub=pub %}
    {% endfor %}
  </ul>
{% endfor %}

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
