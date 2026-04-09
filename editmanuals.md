---
layout: editmanual
title: "Edit Manuals"
description: Edit and preview SEELab manual markdown files
permalink: /editmanuals/
search: exclude
---

<style>
  /* Make the cleancover container span full browser width for this page */
  .manual-wrapper {
    max-width: calc(100vw - 40px) !important;
    width: calc(100vw - 40px) !important;
  }

  /* Preview styles: scoped to the right column so it matches `/_layouts/manual.html` */
  .manual-preview {
    margin: 0;
    background: var(--paper-white, #fff);
    padding: 30px 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border-top: 6px solid var(--seelab-blue, #004a99);
    color: var(--text-dark, #1a1a1a);
    font-family: 'Crimson Pro', serif;
    font-size: 1.15rem;
  }

  .manual-preview .top-bar {
    display: flex;
    justify-content: space-between;
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    text-transform: uppercase;
    font-weight: 700;
    color: #888;
    margin-bottom: 30px;
    letter-spacing: 1.5px;
  }

  .manual-preview .header-title {
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--seelab-blue, #004a99);
    margin: 0 0 10px 0;
    line-height: 1.2;
  }

  .manual-preview .divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--seelab-blue, #004a99), transparent);
    margin-bottom: 30px;
  }

  .manual-preview .info-row {
    display: flex;
    justify-content: space-between;
    margin: 20px 0;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    border-bottom: 1px solid var(--border-light, #dee2e6);
    padding-bottom: 12px;
    font-size: 0.85rem;
  }

  .manual-preview .main-content h3 {
    margin-top: 2.2em;
    color: var(--seelab-blue, #004a99);
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    font-size: 1rem;
    letter-spacing: 0.5px;
    border-left: 4px solid var(--seelab-blue, #004a99);
    padding-left: 12px;
  }

  .manual-preview img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 30px auto;
    border-radius: 4px;
    border: 1px solid var(--border-light, #dee2e6);
  }

  .manual-preview .image-caption {
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    margin-top: -20px;
    margin-bottom: 30px;
    font-style: italic;
  }

  .manual-preview table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
  }
  .manual-preview th,
  .manual-preview td {
    border: 1px solid var(--border-light, #dee2e6);
    padding: 12px;
    text-align: center;
  }
  .manual-preview th {
    background-color: var(--bg-soft, #f8f9fa);
    font-weight: 700;
  }

  .editor-page-wrap {
    width: 100%;
    max-width: 100%;
    padding: 0;
  }

  .editor-toolbar {
    display: flex;
    gap: 10px;
    align-items: center;
    margin: 8px 0 12px 0;
    flex-wrap: wrap;
  }

  .editor-toolbar label {
    font-weight: 600;
    font-family: "Inter", sans-serif;
    font-size: 0.9rem;
  }

  .editor-toolbar select {
    min-width: 340px;
    max-width: 100%;
    padding: 8px 10px;
  }

  .editor-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    width: 100%;
    min-height: 72vh;
  }

  .editor-pane {
    border: 1px solid #d9d9d9;
    border-radius: 6px;
    overflow: hidden;
    background: #fff;
    display: flex;
    flex-direction: column;
    min-height: 72vh;
  }

  .editor-pane-title {
    padding: 8px 12px;
    border-bottom: 1px solid #e9e9e9;
    font-size: 0.84rem;
    font-family: "Inter", sans-serif;
    font-weight: 700;
    color: #4b4b4b;
    background: #f8f9fa;
    letter-spacing: 0.3px;
  }

  #manual-md-editor {
    width: 100%;
    flex: 1;
    min-height: 68vh;
    border: 0;
    outline: none;
    resize: none;
    padding: 12px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 0.86rem;
    line-height: 1.45;
    box-sizing: border-box;
  }

  #manual-html-preview {
    flex: 1;
    min-height: 68vh;
    overflow: auto;
    padding: 1px;
    box-sizing: border-box;
    background: #fff;
  }

  #manual-html-preview > :first-child {
    margin-top: 0;
  }

  @media (max-width: 980px) {
    .editor-grid {
      grid-template-columns: 1fr;
    }
  }

  @media print {
    .editor-toolbar,
    .editor-grid > section:first-child,
    .editor-pane-title {
      display: none !important;
    }
    .editor-grid {
      grid-template-columns: 1fr !important;
      gap: 0 !important;
    }
    .editor-pane {
      border: 0 !important;
      min-height: auto !important;
    }
    #manual-html-preview {
      padding: 0 !important;
    }
    .manual-preview {
      box-shadow: none !important;
      border-top: none !important;
      padding: 0 !important;
    }
  }
</style>

<div class="editor-page-wrap">
  <div class="editor-toolbar">
    <label for="manual-file-select">Manual Markdown File</label>
    <select id="manual-file-select"></select>
  </div>

  <div class="editor-grid">
    <section class="editor-pane">
      <div class="editor-pane-title">Markdown (.md)</div>
      <textarea id="manual-md-editor" spellcheck="false"></textarea>
    </section>

    <section class="editor-pane">
      <div class="editor-pane-title">Rendered HTML Preview</div>
      <div id="manual-html-preview"></div>
    </section>
  </div>
</div>

<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    },
    svg: { fontCache: 'global' }
  };
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  const manualDocs = [
    {% assign manuals = site.seelabmanual | sort: "path" %}
    {% for doc in manuals %}
      {% assign file_name = doc.path | split: "/" | last %}
      {% assign source_path = "/assets/md/" | append: file_name %}
      {
        path: {{ doc.path | jsonify }},
        fileName: {{ file_name | jsonify }},
        sourceUrl: {{ source_path | relative_url | jsonify }},
        title: {{ doc.title | default: doc.path | jsonify }},
        section: {{ doc.section | default: "Technical Manual" | jsonify }},
        imagePath: {{ doc.image.path | default: "" | jsonify }},
        caption: {{ doc.caption | default: "" | jsonify }}
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  const fileSelect = document.getElementById("manual-file-select");
  const mdEditor = document.getElementById("manual-md-editor");
  const htmlPreview = document.getElementById("manual-html-preview");

  function escapeHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  // Prevent the markdown parser from rewriting LaTeX (e.g., "_" -> <em>)
  // We temporarily replace math segments with tokens, parse markdown, then restore.
  function extractMath(md) {
    const store = [];
    let out = md;

    // Block math: $$ ... $$
    out = out.replace(/\$\$([\s\S]*?)\$\$/g, (m) => {
      const key = `@@MATH_BLOCK_${store.length}@@`;
      store.push(m);
      return key;
    });

    // Inline math: $ ... $ (naive, good enough for manuals; ignores escaped dollars)
    out = out.replace(/(^|[^$])\$([^$\n]+?)\$/g, (m, p1) => {
      const full = m.slice(p1.length);
      const key = `@@MATH_INLINE_${store.length}@@`;
      store.push(full);
      return p1 + key;
    });

    return { md: out, store };
  }

  function restoreMath(html, store) {
    let out = html;
    store.forEach((math, i) => {
      out = out
        .replaceAll(`@@MATH_BLOCK_${i}@@`, escapeHtml(math))
        .replaceAll(`@@MATH_INLINE_${i}@@`, escapeHtml(math));
    });
    return out;
  }

  function stripFrontMatter(md) {
    // If markdown starts with YAML front matter, remove it for preview rendering.
    if (!md.startsWith("---")) return md;
    const parts = md.split("\n");
    let endIdx = -1;
    for (let i = 1; i < parts.length; i++) {
      if (parts[i].trim() === "---") {
        endIdx = i;
        break;
      }
    }
    if (endIdx === -1) return md;
    return parts.slice(endIdx + 1).join("\n").trimStart();
  }

  function parseFrontMatter(md) {
    if (!md.startsWith("---")) return {};
    const lines = md.split("\n");
    let endIdx = -1;
    for (let i = 1; i < lines.length; i++) {
      if (lines[i].trim() === "---") {
        endIdx = i;
        break;
      }
    }
    if (endIdx === -1) return {};

    const data = {};
    let parentKey = "";
    for (const raw of lines.slice(1, endIdx)) {
      const line = raw.replace(/\t/g, "  ");
      if (!line.trim() || line.trim().startsWith("#")) continue;

      const nested = line.match(/^ {2}([A-Za-z0-9_-]+):\s*(.*)$/);
      if (nested && parentKey) {
        const key = `${parentKey}.${nested[1]}`;
        data[key] = nested[2].trim().replace(/^["']|["']$/g, "");
        continue;
      }

      const top = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
      if (top) {
        parentKey = top[1];
        data[parentKey] = top[2].trim().replace(/^["']|["']$/g, "");
      }
    }
    return data;
  }

  function renderPreview(docMeta) {
    const md = stripFrontMatter(mdEditor.value || "");
    const extracted = extractMath(md);
    const renderedHtml = marked.parse(extracted.md, { breaks: true });
    const rendered = restoreMath(renderedHtml, extracted.store);

    const sectionText = (docMeta && docMeta.section) ? docMeta.section : "Technical Manual";
    const titleText = (docMeta && docMeta.title) ? docMeta.title : "Manual";
    const imgPath = (docMeta && docMeta.imagePath) ? docMeta.imagePath : "";
    const caption = (docMeta && docMeta.caption) ? docMeta.caption : "";

    htmlPreview.innerHTML = `
      <div class="manual-preview">
        <div class="top-bar">
          <div>${sectionText || "Technical Manual"}</div>
          <div>SEELab User Manual &copy; ${new Date().toLocaleString('en-US', { month: 'short', year: 'numeric' })}</div>
        </div>
        <h1 class="header-title">${titleText}</h1>
        <div class="divider"></div>
        <div class="info-row">
          <span>Name: ______________________</span>
          <span>Exp No: __________, Date: _______</span>
        </div>
        ${imgPath ? `<img src="${imgPath}">` : ""}
        ${(imgPath && caption) ? `<div class="image-caption">${caption}</div>` : ""}
        <div class="main-content">
          ${rendered}
        </div>
      </div>
    `;

    if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetClear && window.MathJax.typesetClear();
      window.MathJax.typesetPromise([htmlPreview]).catch(() => {});
    }
  }

  async function loadDocByIndex(index) {
    const doc = manualDocs[index];
    if (!doc) return;
    const sourceUrl = doc.sourceUrl || `{{ "/assets/md/" | relative_url }}${doc.fileName}`;
    try {
      const res = await fetch(sourceUrl, { cache: "no-store" });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const raw = await res.text();
      mdEditor.value = raw;
      const fm = parseFrontMatter(raw);
      doc.title = fm.title || doc.fileName || "Manual";
      doc.section = fm.section || "Technical Manual";
      doc.imagePath = fm["image.path"] || "";
      doc.caption = fm.caption || "";
    } catch (_) {
      mdEditor.value = `Unable to load: ${sourceUrl}`;
      doc.title = doc.fileName || "Manual";
      doc.section = "Technical Manual";
      doc.imagePath = "";
      doc.caption = "";
    }
    renderPreview(doc);
  }

  function initSelect() {
    manualDocs.forEach((doc, index) => {
      const opt = document.createElement("option");
      opt.value = String(index);
      opt.textContent = doc.fileName || doc.path;
      fileSelect.appendChild(opt);
    });
  }

  fileSelect.addEventListener("change", async () => {
    await loadDocByIndex(Number(fileSelect.value));
  });

  mdEditor.addEventListener("input", () => {
    const doc = manualDocs[Number(fileSelect.value)];
    renderPreview(doc);
  });

  initSelect();
  loadDocByIndex(0);
</script>

