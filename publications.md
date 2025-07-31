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

{% assign type_order = "phdthesis,article,abstract,dataset,eprint,techreport" | split: "," %}

{% for type in type_order %}
  {% assign entries = site.data.ads_publications | where: "entry_type", type %}
  {% if entries.size > 0 %}

  {% capture label %}
    {% case type %}
      {% when "phdthesis" %}PhD Thesis
      {% when "article" %}Peer Reviewed Articles
      {% when "abstract" %}Conference Presentations
      {% when "dataset" %}Dataset
      {% when "eprint" %}Pre-Print
      {% when "techreport" %}White Papers
      {% else %}Other
    {% endcase %}
  {% endcapture %}

  ### {{ label | strip }}

  <ul class="pub-list">
  {% for pub in entries %}
    <li>
      {% assign authors = pub.authors | join: ", " %}
      {% assign bolded_authors = authors %}
      {% assign variants = "Alterman, B. L.|B. Alterman|Benjamin Alterman|Benjamin L. Alterman" | split: "|" %}
      {% for variant in variants %}
        {% assign bolded_authors = bolded_authors | replace: variant, "<strong>" | append: variant | append: "</strong>" %}
      {% endfor %}
      {{ bolded_authors }}.
      "{{ pub.title }}."
      <em>{{ pub.journal }}</em>,
      {{ pub.year }}.
      {% if pub.citation_count > 0 %}Cited {{ pub.citation_count }} times.{% endif %}
      {% if pub.url %} [Link]({{ pub.url }}){% endif %}
    </li>
  {% endfor %}
  </ul>

  {% endif %}
{% endfor %}
