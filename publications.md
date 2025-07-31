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

{% assign pubs = site.data.ads_publications %}

{% assign pubs = pubs | sort: "year" | reverse %}

{% assign grouped = "" | split: "" %}
{% assign pubtypes = "phdthesis,article,inproceedings,abstract,dataset,eprint,techreport" | split: "," %}
{% assign label_map = 
  "phdthesis:PhD Thesis,
   article:Peer Reviewed Articles,
   abstract:Conference Presentations,
   inproceedings:Conference Presentations,
   dataset:Dataset,
   eprint:Pre-Print,
   techreport:White Papers" | split: "," %}

{% assign renamed_types = {} %}
{% for pair in label_map %}
  {% assign parts = pair | split: ":" %}
  {% assign renamed_types = renamed_types | merge: {{ parts[0] | strip }}:{{ parts[1] | strip }} %}
{% endfor %}

{% assign abstracts = pubs | where_exp: "p", "p.publication_type == 'abstract' or p.publication_type == 'inproceedings'" %}
{% assign phdthesis = pubs | where: "publication_type", "phdthesis" %}
{% assign article = pubs | where: "publication_type", "article" %}
{% assign dataset = pubs | where: "publication_type", "dataset" %}
{% assign eprint = pubs | where: "publication_type", "eprint" %}
{% assign techreport = pubs | where: "publication_type", "techreport" %}

{% assign pub_groups = 
  "phdthesis:#{phdthesis},
   article:#{article},
   abstract:#{abstracts},
   dataset:#{dataset},
   eprint:#{eprint},
   techreport:#{techreport}" | split: "," %}

{% for type in pubtypes %}
  {% if type == "inproceedings" %}
    {% continue %}
  {% endif %}
  {% assign group = "" %}
  {% case type %}
    {% when "phdthesis" %}{% assign group = phdthesis %}
    {% when "article" %}{% assign group = article %}
    {% when "abstract" %}{% assign group = abstracts %}
    {% when "dataset" %}{% assign group = dataset %}
    {% when "eprint" %}{% assign group = eprint %}
    {% when "techreport" %}{% assign group = techreport %}
  {% endcase %}
  {% assign label = renamed_types[type] %}
  {% if group.size > 0 %}
  <h2>{{ label }}</h2>
  <ul class="publication-list">
    {% for pub in group %}
      {% assign formatted_authors = "" %}
      {% for author in pub.authors %}
        {% assign parts = author | split: " " %}
        {% assign last = parts[parts.size | minus: 1] %}
        {% assign initials = "" %}
        {% for part in parts %}
          {% unless forloop.last %}
            {% assign first_letter = part | slice: 0, 1 %}
            {% assign initials = initials | append: first_letter | append: "." %}
            {% if forloop.index0 < parts.size | minus: 2 %}
              {% assign initials = initials | append: " " %}
            {% endif %}
          {% endunless %}
        {% endfor %}
        {% assign formatted_name = last | append: ", " | append: initials %}
        {% if author contains "Alterman" %}
          {% assign formatted_name = "<strong>" | append: formatted_name | append: "</strong>" %}
        {% endif %}
        {% assign formatted_authors = formatted_authors | append: formatted_name %}
        {% unless forloop.last %}
          {% assign formatted_authors = formatted_authors | append: ", " %}
        {% endunless %}
      {% endfor %}
      <li>
        <strong><a href="{{ pub.url }}" target="_blank" rel="noopener">{{ pub.title }}</a></strong><br>
        <span class="authors">{{ formatted_authors }}</span><br>
        <em>{{ pub.journal }}</em>, {{ pub.year }}.
        {% if pub.citations and pub.citations > 0 %}
          <span class="citations"> Citations: {{ pub.citations }}</span>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
  {% endif %}
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
