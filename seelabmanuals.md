---
layout: cleancover
title: "SEELab 3.0 : Lab Manuals"
description: Printable docs for Experiments with SEELab 3.0
lang: en
date: 28 March 2026
image:
  path: /assets/img/phd/seelab-cover.jpg
caption: Traditional lab manuals for SEElab 3.0
---

<div style="padding: 20px;">  
  {% assign toc_lang = page.lang | default: "en" %}
  {% assign available_langs = "" %}
  {% for d in site.seelabmanual %}
    {% assign l = d.lang | default: "en" %}
    {% assign token = l | append: "," %}
    {% unless available_langs contains token %}
      {% assign available_langs = available_langs | append: token %}
    {% endunless %}
  {% endfor %}

  {% assign langs_arr = available_langs | split: "," %}
  <div class="no-print" style="text-align: center; margin: 0 0 14px; font-family: 'Inter', sans-serif; font-size: 0.78rem; letter-spacing: 0.4px;">
    {% for l in langs_arr %}
      {% if l != "" %}
        {% assign toc_url = "" %}
        {% assign toc_doc = nil %}
        {% if l == "en" %}
          {% assign toc_url = "/seelabmanuals" %}
        {% else %}
          {% assign toc_perm = "/" | append: l | append: "/seelabmanuals/" %}
          {% assign toc_doc = site.pages | where: "permalink", toc_perm | first %}
          {% assign toc_url = "/" | append: l | append: "/seelabmanuals/" %}
        {% endif %}

        {% if l == toc_lang or l == "en" or toc_doc %}
          {% unless forloop.first %} | {% endunless %}
          {% if l == toc_lang %}
            <strong>{{ l | upcase }}</strong>
          {% else %}
            <a href="{{ toc_url | relative_url }}">{{ l | upcase }}</a>
          {% endif %}
        {% endif %}
      {% endif %}
    {% endfor %}
  </div>

  {% assign ordered = site.data.manual_book_order.manual_order | default: "" %}
  {% for section_name in site.manual_sections %}
    {% assign section_count = 0 %}
    {% for slug in ordered %}
      {% assign item = nil %}
      {% assign wanted_key = slug | downcase %}
      {% for d in site.seelabmanual %}
        {% assign doc_key = d.slug | default: d.basename | default: d.name | default: d.path %}
        {% assign doc_key = doc_key | downcase | replace: ".md", "" %}
        {% if doc_key == wanted_key %}
          {% assign item = d %}
          {% break %}
        {% endif %}
      {% endfor %}
      {% if item and item.section == section_name %}
        {% assign item_lang = item.lang | default: "en" %}
        {% if item_lang == toc_lang %}
          {% assign section_count = section_count | plus: 1 %}
        {% endif %}
      {% endif %}
    {% endfor %}

    {% if section_count > 0 %}
      <h3 style="color: var(--seelab-blue); font-size: 0.9rem; text-transform: uppercase; border-bottom: 2px solid var(--seelab-blue); padding-bottom: 5px; margin-top: 25px; display: flex; justify-content: space-between;">
        {{ section_name }}
        <span style="font-size: 0.7rem; opacity: 0.6;">{{ section_count }} Units</span>
      </h3>      
      <ul style="list-style: none; padding: 0; margin: 0;">
        {% for slug in ordered %}
          {% assign item = nil %}
          {% assign wanted_key = slug | downcase %}
          {% for d in site.seelabmanual %}
            {% assign doc_key = d.slug | default: d.basename | default: d.name | default: d.path %}
            {% assign doc_key = doc_key | downcase | replace: ".md", "" %}
            {% if doc_key == wanted_key %}
              {% assign item = d %}
              {% break %}
            {% endif %}
          {% endfor %}
          {% if item and item.section == section_name %}
            {% assign item_lang = item.lang | default: "en" %}
            {% if item_lang == toc_lang %}
              <li style="border-bottom: 1px solid #f0f0f0;">
                <a href="{{ item.url | relative_url }}" style="text-decoration: none; color: #333; display: flex; align-items: center; padding: 10px 5px 10px 5px; border-radius: 4px; transition: all 0.2s;" onmouseover="this.style.background='#f8f9fa'; this.style.paddingLeft='10px'" onmouseout="this.style.background='transparent'; this.style.paddingLeft='5px'">
                  <div style="flex-grow: 1; font-weight: 600; font-size: 1rem;">
                    {{ item.title }}
                  </div>
                  <span style="color: var(--seelab-blue); font-size: 1.2rem; font-weight: bold; opacity: 0.3;">&rsaquo;</span>
                </a>
              </li>
            {% endif %}
          {% endif %}
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}

  {% assign unsectioned_count = 0 %}
  {% for slug in ordered %}
    {% assign item = nil %}
    {% assign wanted_key = slug | downcase %}
    {% for d in site.seelabmanual %}
      {% assign doc_key = d.slug | default: d.basename | default: d.name | default: d.path %}
      {% assign doc_key = doc_key | downcase | replace: ".md", "" %}
      {% if doc_key == wanted_key %}
        {% assign item = d %}
        {% break %}
      {% endif %}
    {% endfor %}
    {% if item and item.section == nil %}
      {% assign item_lang = item.lang | default: "en" %}
      {% if item_lang == toc_lang %}
        {% assign unsectioned_count = unsectioned_count | plus: 1 %}
      {% endif %}
    {% endif %}
  {% endfor %}

  {% if unsectioned_count > 0 %}
    <h3 style="color: #666; font-size: 0.9rem; text-transform: uppercase; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 25px;">Miscellaneous</h3>
    <ul style="list-style: none; padding: 0; margin: 0;">
      {% for slug in ordered %}
        {% assign item = nil %}
        {% assign wanted_key = slug | downcase %}
        {% for d in site.seelabmanual %}
          {% assign doc_key = d.slug | default: d.basename | default: d.name | default: d.path %}
          {% assign doc_key = doc_key | downcase | replace: ".md", "" %}
          {% if doc_key == wanted_key %}
            {% assign item = d %}
            {% break %}
          {% endif %}
        {% endfor %}
        {% if item and item.section == nil %}
          {% assign item_lang = item.lang | default: "en" %}
          {% if item_lang == toc_lang %}
            <li style="margin: 8px 0;"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
          {% endif %}
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}

</div>

