---
title: "System Options > Export > TIF/PSD/JPG/PNG"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAsTIFPSDOptions.htm"
---

# System Options > Export > TIF/PSD/JPG/PNG

To display the dialog:

Click **Tools > Options > System Options > Export > TIF/PSD/JPG/PNG** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Tif**, **Adobe PhotoShop File**s, **JPEG**, or **Portable Network Graphics**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value> or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Output as - Image type | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffImageType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffImageType, swTiffImageType_e.< Value >) | See swTiffImageType_e for valid options |  |
| Output as - Tiff Compression scheme | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffCompressionScheme) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffCompressionScheme, swTiffCompressionScheme_e.< Value >) | See swTiffCompressionScheme_e for valid options |  |
| Output as - Remove background | See Comment | See Comment | Currently not available in the SOLIDWORKS API |
| Output as - Jpeg Compression | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportJpegCompression) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swExportJpegCompression, < Value >) | Long value (1-100) | 1 is for lowest compression; 100 is for highest compression (low quality) |
| Output as - Screen capture | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffScreenOrPrintCapture) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffScreenOrPrintCapture, < Value >) | 0 |  |
| Output as - Print capture | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffScreenOrPrintCapture) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffScreenOrPrintCapture, < Value >) | 1 |  |
| Output as - All sheets (multipage) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintAllSheets) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintAllSheets, < OnFlag >) | True | For Output as - Print capture only |
| Output as - Current sheet | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintAllSheets) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintAllSheets, < OnFlag >) | False | For Output as - Print capture only |
| Output as - Use sheet size(s) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintUseSheetSize) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintUseSheetSize, < OnFlag >) | True | For Output as - Print capture only |
| Output as - Use print size | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintUseSheetSize) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintUseSheetSize, < OnFlag >) | False | For Output as - Print capture only |
| Output as - Enable text padding (for low DPI/size settings) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintPadText) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintPadText, < OnFlag >) | Boolean value | Adjusts inter-character text spacing such that the text fills the bounding rectangle of the string; set to True when using low DPI and small paper sizes (A, A4, or A3) |
| Output as - Include layers set not to print | SldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTIFIncludeLayersNotToPrint) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTIFIncludeLayersNotToPrint, < OnFlag >) | Boolean value | Specifies whether to include layers set not to print |
| Output as - Include drawings paper color | SldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTIFExportIncludeDrawingsPaperColor) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTIFExportIncludeDrawingsPaperColor, < OnFlag >) | Boolean value |  |
| Print capture options - DPI | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintDPI) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintDPI, < Value >) | Integer value | For drawings only; For Output as - Print capture only |
| Print capture options - Paper size | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintPaperSize) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintPaperSize, swDwgPaperSizes_e.< Value >) | See swDwgPaperSizes_e for valid options |  |
| Print capture options - Width | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swTiffPrintDrawingPaperWidth) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swTiffPrintDrawingPaperWidth, < Value >) | Double value in meters | For drawings only; For Output as - Print capture only with Print capture options - Paper size set to User Defined |
| Print capture options - Height | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swTiffPrintDrawingPaperHeight) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swTiffPrintDrawingPaperHeight, < Value >) | Double value in meters | For drawings only; For Output as - Print capture only with Print capture options - Paper size set to User Defined |
| Print capture options - Scale to fit | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintScaleToFit) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTiffPrintScaleToFit, < OnFlag >) | Boolean value | For drawings only; specifies whether to scale drawing to fit page |
| Print capture options - Scale | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintScaleFactor) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swTiffPrintScaleFactor, < Value >) | Integer value | Specifies the scale factor |
