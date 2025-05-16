---
layout: archive
title: 
permalink: /CV/
author_profile: true
redirect_from:
  - /CV
---

{% include base_path %}

<div class="wrapper">
  <div id="pdf-wrapper">
    <div id="adobe-dc-view"></div>
  </div>

  <a
    href="https://manuelacollis.com/files/current_CV_Manuela_R_Collis.pdf"
    class="download-btn"
    download
    target="_blank"
  >
    Click here to download the CV.
  </a>
</div>

<!-- Adobe Viewer SDK -->
<script src="https://acrobatservices.adobe.com/view-sdk/viewer.js"></script>
<script type="text/javascript">
  document.addEventListener("adobe_dc_view_sdk.ready", function () {
    const adobeDCView = new AdobeDC.View({
      clientId: "f1f319d22b0945059978e7d5039b772e",
      divId: "adobe-dc-view"
    });

    adobeDCView.previewFile({
      content: {
        location: {
          url: "https://manuelacollis.com/files/current_CV_Manuela_R_Collis.pdf"
        }
      },
      metaData: {
        fileName: "CV_Manuela_R_Collis.pdf"
      }
    }, {
      embedMode: "IN_LINE",
      showDownloadPDF: true,
      showPrintPDF: true,
      showFullScreen: true
    });
  });
</script>

<style>
  body {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    background-color: #ffffff;
  }

  .wrapper {
    width: 800px;
    margin: 100px auto;
  }

  #pdf-wrapper {
    width: 100%;
    height: 90vh;
    overflow-y: auto;
    box-shadow: 1px 1px 10px 1px #dadada;
  }

  .download-btn {
    display: block;
    margin: 30px auto 80px auto;
    padding: 12px 20px;
    font-size: 16px;
    color: #333;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-decoration: none;
    text-align: center;
    width: fit-content;
    transition: background-color 0.3s ease;
  }

  .download-btn:hover {
    background-color: #e6e6e6;
  }

  @media (max-width: 900px) {
    .wrapper {
      width: 95%;
      margin: 40px auto;
    }

    #pdf-wrapper {
      height: 85vh;
    }

    .download-btn {
      font-size: 14px;
      padding: 10px 16px;
    }
  }
</style>