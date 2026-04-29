---
layout: project
title: "SEELab 3.0 : Blog"
description: Blog posts pertaining to SEELab 3.0
lang: en
date: 28 March 2026
image:
  path: /assets/img/phd/seelab-cover.jpg
caption: Blog posts on SEElab 3.0
---

<div style="padding: 20px;">
  {% assign toc_lang = page.lang | default: "en" %}
  {% assign posts = site.seelabblog | sort: "date" | reverse %}

  <div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
    {% for post in posts %}
      {% assign item_lang = post.lang | default: "en" %}
      {% if item_lang == toc_lang %}
        {% assign featured = page.featured | default:post.featured | default:page.big_project | default:post.big_project %}
        <div class="column column-1">
          {% include_cached pro/post-card.html post=post featured=featured %}
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>

