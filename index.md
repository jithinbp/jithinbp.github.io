---
layout: welcome
image: /assets/img/cover.jpg
hide_description: true
---

# Hello, Fellow traveller! 🥸

> I work with design and development, as well as bulk manufacturing of electronics.
  This website describes many of my hacks/creations. 
  * All my startup related work is at [CSpark Research](https://csparkresearch.in)
  * Ph.D in Nuclear Physics instrumentation - development of radiation detection equipment. 
  * Founded CSpark Research for developing affordable data acquisition instruments for schools and colleges.
  * Master's in Physics from IISER-M with thesis work on Point Contact Spectroscopy and Scanning Tunnelling microscopy.



* My Rather Incomplete [Resume](/resume.md){:.heading.flip-title}
{:.related-posts.faded}


## Manufacturing Experience | <a class="heading flip-title" href="/build/" style="color:teal"> Posts<sup>[{{ site.manufacturing | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.manufacturing | sort:"date" | reverse %}
{% for project in ordered_projects limit:5 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 custommicrocol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>


## Recent Projects | <a class="heading flip-title" href="/projects/" style="color:teal"> Posts<sup>[{{ site.projects | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.projects | sort:"date" | reverse %}
{% for project in ordered_projects limit:10 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 custommicrocol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>




## Ph.D Thesis @ CUHP  /  My Startup <a href="https://csparkresearch.in" target="_blank">csparkresearch.in</a> | <a class="heading flip-title" href="/phd/" style="color:teal">All Posts<sup>[{{ site.phd | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.phd | sort:"date" | reverse %}
{% for project in ordered_projects limit:6 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 customcol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

<!---<p class="read-more mt1"><a class="heading flip-title" href="/iiser/">More from my Ph.D. work <sup>[{{ site.phd | size }}]</sup></a></p> -->



## Master's Thesis @ IISER-M | <a class="heading flip-title" href="/iiser/" style="color:teal">  Posts<sup>[{{ site.iiser | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiser | sort:"date" | reverse %}
{% for project in ordered_projects limit:8 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 customcol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

<!-- <p class="read-more mt1"><a class="heading flip-title" href="/iiser/">More from MS Thesis at IISER <sup>[{{ site.iiser | size }}]</sup></a></p> -->

### Other Projects while @ IISER-M | <a class="heading flip-title" href="/iiseracad/" style="color:teal"> Posts<sup>[{{ site.iiseracad | size }}]</sup></a>

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiseracad | sort:"date"%}
{% for project in ordered_projects limit:10 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 custommicrocol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

<!-- <p class="read-more mt1"><a class="heading flip-title" href="/iiseracad/">Click here to check out my other undergrad projects <sup>[{{ site.iiseracad | size }}]</sup></a></p> -->



## Hobby Projects | <a class="heading flip-title" href="/hobbies/" style="color:teal"> All<sup>[{{ site.hobby | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.hobby | sort:"date" | reverse %}
{% for project in ordered_projects limit:3 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 customcol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}

</div>

<!--<p class="read-more mt1"><a class="heading flip-title" href="/hobbies/">More random things<sup>[{{ site.hobby | size }}]</sup></a></p> -->


