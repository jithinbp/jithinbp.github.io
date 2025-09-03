---
layout: projects
title: Academic Projects at IISER Mohali
---


<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiseracad | sort:"date"%}
{% for project in ordered_projects %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

<p class="read-more mt1"><a class="heading flip-title" href="/iiser/">Click here to view my MS thesis related posts instead</a></p>

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiser | sort:"date"%}
{% for project in ordered_projects limit:3 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>


