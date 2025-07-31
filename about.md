---
layout: single
title: About
permalink: /about/
description: Ben Alterman is a NASA Research Astrophysicist studying the solar wind, space weather, and humanity’s place in the heliosphere using data from Wind, ACE, Parker Solar Probe, and Solar Orbiter.
author: B. L. Alterman
image: /assets/images/headshot.jpg
---

Ben Alterman is a Research Astrophysicist at NASA’s Goddard Space Flight Center. He earned his PhD in Applied Physics from the University of Michigan, where he explored how Coulomb collisions and kinetic processes shape the solar wind. After completing a postdoc at the Southwest Research Institute in San Antonio—where he was promoted to Research Scientist—Ben transitioned to civil service at NASA, continuing his work in heliophysics.

Ben is a heliophysics generalist with broad expertise in the thermal and suprathermal solar wind. His research spans multiple spacecraft—including Wind, ACE, Parker Solar Probe, and Solar Orbiter—and multiple timescales, from the second-by-second dynamics of kinetic instabilities to long-term variations across solar cycles. He’s published widely on solar wind composition, solar sources of the solar wind, and the role of helium as a diagnostic of solar activity.

At heart, Ben is driven by the big questions: What powers the solar wind? How do kinetic signatures reflect global solar evolution? And how do small-scale processes connect to the larger heliospheric system? He brings a dynamic interest in our Sun, humanity’s place in the Universe, and the ways solar variability influences life on Earth through space weather. A Fellow of The Explorers Club and an active member of the heliophysics community, he approaches these challenges with curiosity, technical depth, and creative thinking.

You can find my research profiles at the links below. My publications are available [here](/publications/).

- <img src="/assets/images/orcid/ORCID-iD_icon_24x24.png" alt="ORCID logo" width="20" height="20"> [ORCID](https://orcid.org/{{ site.ads_orcid }})
- <img src="/assets/images/ads/ads.svg" alt="NASA ADS logo" width="20" height="20"> [NASA ADS](https://ui.adsabs.harvard.edu/search/q=orcid%3A{{ site.ads_orcid }}&sort=date%20desc,%20bibcode%20desc&p_=0)
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
</section>
