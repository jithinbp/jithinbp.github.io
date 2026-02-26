---
layout: welcome
image: /assets/img/cover.jpg
hide_description: true

---

# Hello, Fellow traveller! 🥸

<style>
.image-card-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: baseline;
  gap: 15px;
  margin: 20px 0;
}

.image-card {
  flex: 1;
  min-width: 80px;
  max-width: 120px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 8px;
  overflow: hidden;
  background: var(--gray-bg, #f5f5f5);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.image-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.image-card a {
  text-decoration: none;
  color: inherit;
  display: block;
}

.image-card img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  aspect-ratio: 1.43;
}

.image-card-caption {
  padding: 2px;
  font-size: 0.9rem;
  color: var(--gray-text, #333);
  margin: 0;
}

@media (max-width: 1200px) {
  .image-card {
    min-width: calc(25% - 8px);
    max-width: calc(25% - 8px);
  }
}


@media (max-width: 768px) {
  .image-card {
    min-width: calc(25% - 8px);
    max-width: calc(25% - 8px);
  }
}

@media (max-width: 480px) {
  .image-card {
    min-width: calc(25% - 8px);
    max-width: calc(25% - 8px);
  }
}
</style>

<div class="image-card-row">
  <div class="image-card">
    <a href="https://csparkresearch.in" target="_blank" class="no-mark">
      <img src="/assets/img/cspark.png" alt="Card 1">
      <p class="image-card-caption">My Startup</p>
    </a>
  </div>
  <div class="image-card">
    <a href="#masters-thesis--iiser-m--8">
      <img src="/assets/img/pcar/thermal.png" alt="Card 2">
      <p class="image-card-caption">BS-MS @ IISER-M</p>
    </a>
  </div>
  <div class="image-card">
    <a href="/phd/">
      <img src="/assets/img/phd/coincidence.webp" alt="Card 3">
      <p class="image-card-caption">PhD @ CUHP</p>
    </a>
  </div>
  <div class="image-card">
    <a href="/build/">
      <img src="/assets/img/blog/cvphoto.jpg" alt="Card 4">
      <p class="image-card-caption">CMNPDF @ UoC</p>
    </a>
  </div>
  <div class="image-card">
    <a href="/build/">
      <img src="/assets/img/blog/man.webp" alt="Card 5">
      <p class="image-card-caption">Manufacturing</p>
    </a>
  </div>
  <div class="image-card">
    <a href="#recent-projects--29">
      <img src="/assets/img/blog/st.webp" alt="Card 6">
      <p class="image-card-caption">Projects</p>
    </a>
  </div>
</div>


I work with design and development, as well as bulk manufacturing of electronics. Founded [CSpark Research](https://csparkresearch.in) for developing affordable data acquisition instruments for schools and colleges.
BS-MS from IISER Mohali with thesis work on Point Contact Spectroscopy and Scanning Tunnelling microscopy, Nuclear Physics instrumentation Ph.D. from CUHP, Post Doc UoC. A Rather Incomplete [Resume](/resume.md){:.heading.flip-title}


## Manufacturing Memoirs | <a class="heading flip-title" href="/build/" style="color:teal"><sup>[{{ site.manufacturing | size }}]</sup></a>
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

{% assign psize = site.manufacturing.size %}
{% if psize > 5 %}
<p class="read-more mt1"><a class="heading flip-title" href="/build/">{{ site.manufacturing.size | minus:5 }} more posts</a></p>
{% endif %}

## Recent Projects | <a class="heading flip-title" href="/projects/" style="color:teal"><sup>[{{ site.projects | size }}]</sup></a>
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.projects | sort:"date" | reverse %}
{% for project in ordered_projects limit:15 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1 custommicrocol">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>
{% assign psize = site.projects.size %}
{% if psize > 15 %}
<p class="read-more mt1"><a class="heading flip-title" href="/projects/">{{ site.projects.size | minus:15 }} more projects</a></p>
{% endif %}




## Ph.D Thesis @ CUHP  /  My Startup <a href="https://csparkresearch.in" target="_blank">csparkresearch.in</a> | <a class="heading flip-title" href="/phd/" style="color:teal"><sup>[{{ site.phd | size }}]</sup></a>
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
{% assign psize = site.phd.size %}
{% if psize > 6 %}
<p class="read-more mt1"><a class="heading flip-title" href="/phd/">{{ site.phd.size | minus:6 }} more posts</a></p>
{% endif %}

<!---<p class="read-more mt1"><a class="heading flip-title" href="/iiser/">More from my Ph.D. work <sup>[{{ site.phd | size }}]</sup></a></p> -->



## Master's Thesis @ IISER-M | <a class="heading flip-title" href="/iiser/" style="color:teal"><sup>[{{ site.iiser | size }}]</sup></a>
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

{% assign psize = site.iiser.size %}
{% if psize > 8 %}
<p class="read-more mt1"><a class="heading flip-title" href="/iiser/">{{ site.iiser.size | minus:8 }} more projects</a></p>
{% endif %}


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

{% assign psize = site.iiseracad.size %}
{% if psize > 10 %}
<p class="read-more mt1"><a class="heading flip-title" href="/iiseracad/">{{ site.iiseracad.size | minus:10 }} more random things</a></p>
{% endif %}

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

{% assign psize = site.hobby.size %}
{% if psize > 3 %}
<p class="read-more mt1"><a class="heading flip-title" href="/hobbies/">{{ site.hobby.size | minus:10 }} more posts</a></p>
{% endif %}

<!--<p class="read-more mt1"><a class="heading flip-title" href="/hobbies/">More random things<sup>[{{ site.hobby | size }}]</sup></a></p> -->


