---
layout: projects
title: Fabrication Flex 💪✨
screenshot: /assets/img/seminar/seminar_cropped-1-38_page-0024_clipped.jpg
---

### The various manufacturing tools and techniques that I have hands-on experience with


<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.manufacturing | sort:"date" | reverse %}
{% for project in ordered_projects %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>
