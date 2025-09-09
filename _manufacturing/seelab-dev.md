---
layout: project
title: Development History of ExpEYES-17 / SEELab-3
screenshot: /assets/img/seelab/dev/8.jpg
caption: My work from 2014 onwards on FOSS hardware ExpEYES17/SEElab3
description: >
  describes the development of ExpEYES-17, vLabtool, PSLab, Python Powered Scientific instrumentation tool, and SEELab-3. From 2014 onwards. Documented in detail on Hackaday.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#40182a 0%,#3d1d3c 30%,#e700ff 50%,#9900e9 70%,#008729 100%)'
  overlay:    true

---

The circuits layouts were prepared by my father Dr Ajith Kumar, and I worked on the remaining bits which include soldering boards, firmware development, software work such as python libraries, graphical interfaces etc. For enclosure designs, I frequented various shops in Paharganj, New Delhi which dealt in laser cut signboards, and had nice tools.

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign prototypes = site.data.expeyes-dev %}

{% for prototype in prototypes %}
    <div class="column column-1 customcol">

      <article
        class="project-card">
        <a class="no-hover no-print-link flip-project" tabindex="-1">
          <div class="project-card-img aspect-ratio sixteen-nine flip-project-img {% unless screenshot %}fallback-img{% endunless %}">
            {% include_cached components/hy-img.html img=prototype.url alt=prototype.date sizes=sizes width=864 height=486 %}
          </div>
        </a>
        <h3 class="project-card-title flip-project-title">
          <a class="flip-title" property="mainEntityOfPage">{{ prototype.date }}</a>
        </h3>
          <div class="project-card-text fine" property="disambiguatingDescription">
            {{ prototype.description  }}
          </div>
      </article>

    </div>
{% endfor %}
</div>

