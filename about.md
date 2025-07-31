---
layout: single
title: About
permalink: /about/
---
<p>Add your introductory paragraph here.</p>
<p>Add a second paragraph about yourself here.</p>

You can find my research profiles and publications at the links below:

- <img src="/assets/images/orcid/ORCID-iD_icon_24x24.png" alt="ORCID logo" width="20" height="20"> [ORCID {{ ENV.ADS_ORCID }}](https://orcid.org/{{ ENV.ADS_ORCID }})
- <img src="/assets/images/ads/ads.svg" alt="NASA ADS logo" width="20" height="20"> [NASA ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A{{ ENV.ADS_ORCID }}&sort=date%20desc,%20bibcode%20desc&p_=0)
- <img src="/assets/images/google-scholar/google-scholar.svg" alt="Google Scholar logo" width="20" height="20"> [Google Scholar](https://scholar.google.com/citations?user=yF0j6J8AAAAJ)
- <img src="/assets/images/arxiv/arxiv.svg" alt="arXiv logo" width="20" height="20"> [arXiv](https://arxiv.org/a/alterman_b_1)
- <img src="/assets/images/github/github-mark.svg" alt="GitHub logo" width="20" height="20"> [GitHub](https://github.com/blalterman)

<section class="about-columns">
  <div class="about-right">
    <h2>Education</h2>
    <table class="education-table">
      <thead>
        <tr>
          <th>Institution</th>
          <th>Department</th>
          <th>Location</th>
          <th>Dates</th>
        </tr>
      </thead>
      <tbody>
        {% for edu in site.data.education %}
        <tr>
          <td>{{ edu.Institution }}</td>
          <td>{{ edu.Department }}</td>
          <td>{{ edu.Location }}</td>
          <td>{{ edu.Dates }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    <h2>Experience</h2>
<table class="positions-table">
  <thead>
    <tr>
      <th>Title</th>
      <th>Company</th>
      <th>Dates</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    {% for pos in site.data.positions %}
    <tr>
      <td>{{ pos["Position Title"] }}</td>
      <td>{{ pos.Company }}</td>
      <td>{{ pos.Dates }}</td>
      <td>{{ pos.Location }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
  </div>
</section>
