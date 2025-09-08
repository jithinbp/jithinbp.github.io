---
layout: projects
title: Development History of ExpEYES-17
image:  
  path: /assets/img/pcar/thermal.png
screenshot: /assets/img/pcar/thermal.png
caption: My work from 2014 onwards on FOSS hardware
description: >
  describes the development of ExpEYES-17, vLabtool, PSLab, Python Powered Scientific instrumentation tool, and SEELab-3. From 2014 onwards. Documented in detail on Hackaday.
---

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

