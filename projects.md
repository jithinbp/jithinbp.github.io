---
layout: projects
title: Projects
description: >
  Other stuff I worked on
no_groups: true
---



<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.projects | sort:"date" | reverse %}
{% for project in ordered_projects %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>
