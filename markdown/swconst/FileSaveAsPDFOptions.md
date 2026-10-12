---
title: "System Options > Export > PDF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsPDFOptions.htm"
---

# System Options > Export > PDF

To display the dialog:

Click **Tools > Options > System Options > Export > PDF** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Adobe Portable Document Format**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Export PDF in color | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportInColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportInColor, < OnFlag >) | Boolean value | Specifies whether to save documents in color when saving to PDF |
| Embed fonts | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportEmbedFonts) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportEmbedFonts, < OnFlag >) | Boolean value | Specifies whether to embed fonts when saving documents to PDF |
| High quality lines | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportHighQuality) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportHighQuality, < OnFlag >) | Boolean value | Specifies whether to save drawing documents in high quality when saving to PDF |
| Shaded/Draft geometry DPI | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPDFExportShadedDraftDPI) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPDFExportShadedDraftDPI, < Value >) | Integer value | For drawings only; controls dots per inch (DPI) setting for shaded and draft geometry; increased value improves quality while increasing the file size and the time to save the file |
| Sharpened OLE DPI | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPDFExportOleDPI) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swPDFExportOleDPI, < Value >) | Integer value | For drawings only; controls DPI setting for Object Linking and Embedding (OLE) objects; increased value improves quality while increasing the file size and the time to save the file |
| High quality shaded edges | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportShadedEdgesHighQuality) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportShadedEdgesHighQuality, < OnFlag >) | Boolean value |  |
| Print header/footer | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportPrintHeaderFooter) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportPrintHeaderFooter, < OnFlag >) | Boolean value | Specifies whether to use the header and footer specified in File > Print > Header Footer when saving documents to PDF |
| Use specified printer line weights ( File > Print > Line Weights ) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportUseCurrentPrintLineWeights) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportUseCurrentPrintLineWeights, < OnFlag >) | Boolean value | Specifies whether to use the default printer line weights when saving documents to PDF |
| Include layers set to not print | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportIncludeLayersNotToPrint) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportIncludeLayersNotToPrint, < OnFlag >) | Boolean value | Specifies whether to include layers set not to print |
| Include drawings paper color | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportIncludeDrawingsPaperColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPDFExportIncludeDrawingsPaperColor, < OnFlag >) | Boolean value |  |
