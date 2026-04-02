---
layout: cleancover
title: "SEELab 3.0 : Lab Manuals"
date: 28 March 2026
image:
  path: /assets/img/phd/seelab-cover.jpg
caption: Traditional lab manuals for SEElab 3.0
---

<div style="padding: 20px;">  
  {% for section_name in site.manual_sections %}
    {% assign section_items = site.seelabmanual | where: "section", section_name | sort: "date" %}    
    {% if section_items.size > 0 %}
      <h3 style="color: var(--seelab-blue); font-size: 0.9rem; text-transform: uppercase; border-bottom: 2px solid var(--seelab-blue); padding-bottom: 5px; margin-top: 25px; display: flex; justify-content: space-between;">
        {{ section_name }}
        <span style="font-size: 0.7rem; opacity: 0.6;">{{ section_items.size }} Units</span>
      </h3>      
      <ul style="list-style: none; padding: 0; margin: 0;">
        {% for item in section_items %}
          <li style="border-bottom: 1px solid #f0f0f0;">
            <a href="{{ item.url | relative_url }}" style="text-decoration: none; color: #333; display: flex; align-items: center; padding: 10px 5px; border-radius: 4px; transition: all 0.2s;" onmouseover="this.style.background='#f8f9fa'; this.style.paddingLeft='10px'" onmouseout="this.style.background='transparent'; this.style.paddingLeft='5px'">
              <div style="flex-grow: 1;">
                <div style="font-weight: 600; font-size: 1rem;">{{ item.title }}</div>
                <div style="font-size: 0.75rem; color: #888;">{{ item.date | date: "%B %d, %Y" }}</div>
              </div>
              <span style="color: var(--seelab-blue); font-size: 1.2rem; font-weight: bold; opacity: 0.3;">&rsaquo;</span>
            </a>
          </li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
  {% assign unsectioned = site.seelabmanual | where_exp: "item", "item.section == nil" %}
  {% if unsectioned.size > 0 %}
    <h3 style="color: #666; font-size: 0.9rem; text-transform: uppercase; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 25px;">Miscellaneous</h3>
    <ul style="list-style: none; padding: 0; margin: 0;">
      {% for item in unsectioned %}
        <li style="margin: 8px 0;"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
      {% endfor %}
    </ul>
  {% endif %}

</div>

