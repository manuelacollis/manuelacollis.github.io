---
layout: archive
title: "Resume"
permalink: /resume/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<object data="files/current_CV_Manuela_R_Collis.pdf" type="application/pdf" width="100%" height="600px">
  <p>Your browser does not support PDFs. <a href="files/current_CV_Manuela_R_Collis.pdf">Download the PDF</a> instead.</p>
</object>



<embed src="files/current_CV_Manuela_R_Collis.pdf" type="application/pdf" width="100%" height="600px" />



<div id="pdf-viewer" style="width: 100%; height: 600px;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.min.js"></script>
<script>
  // The workerSrc property needs to be specified
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.worker.min.js';

  // Path to your PDF
  const pdfUrl = 'files/current_CV_Manuela_R_Collis.pdf';
  
  // Create the PDF viewer
  const loadingTask = pdfjsLib.getDocument(pdfUrl);
  loadingTask.promise.then(function(pdf) {
    // Create a container for pages
    const container = document.getElementById('pdf-viewer');
    container.style.overflow = 'auto';
    
    // Load first page initially
    pdf.getPage(1).then(function(page) {
      const scale = 1.5;
      const viewport = page.getViewport({ scale: scale });
      
      // Prepare canvas using PDF page dimensions
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      canvas.height = viewport.height;
      canvas.width = viewport.width;
      container.appendChild(canvas);
      
      // Render PDF page into canvas context
      const renderContext = {
        canvasContext: context,
        viewport: viewport
      };
      page.render(renderContext);
    });
    
    // You could add navigation controls here if needed
  });
</script>


<div id="viewer" style="width: 100%; height: 500px;"></div>
<script type="text/javascript" src="https://cloudpdf.io/viewer.min.js"></script>
<script>
  const config = { 
    documentId: 'c724b57e-8e2b-49cd-bdca-34eb176c2709',
    darkMode: true, 
  };
  CloudPDF(config, document.getElementById('viewer')).then((instance) => {
    
  });
</script>


<!-- 
Go here to upload a new version of my CV:
https://www.embedpdf.com/org/7357/document/3436620a-4753-4b8f-bae8-dbea7d49bace/embed

-->

[You can download my resume here](http://manuelacollis.github.io/files/current_CV_Manuela_R_Collis.pdf)



