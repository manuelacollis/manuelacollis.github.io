---
layout: archive
title: "Resume"
permalink: /resume/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
<div id="adobe-dc-view" style="width: 100%; height: 600px;"></div>
<script src="https://documentservices.adobe.com/view-sdk/viewer.js"></script>
<script>
  document.addEventListener("adobe_dc_view_sdk.ready", function() {
    var adobeDCView = new AdobeDC.View({
      clientId: "c35864c7b0b74a69a5d16c7675918c3b",
      divId: "adobe-dc-view"
    });
    adobeDCView.previewFile({
      content: {
        location: {
          url: "https://manuelacollis.github.io/files/current_CV_Manuela_R_Collis.pdf"
        }
      },
      metaData: {fileName: "CV_Manuela_R_Collis.pdf"}
    }, {
      embedMode: "SIZED_CONTAINER",
      showDownloadPDF: true,
      showPrintPDF: true,
      showFullScreen: true
    });
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



