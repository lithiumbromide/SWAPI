---
title: "System Options > Export > 3DPDF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAs3DPDFOptions.htm"
---

# System Options > Export > 3DPDF

To display the dialog:

Click **Tools > Options > System Options > Export > 3DPDF** in **File Format**.

- or -

1. Click **File > Save As**.
2. In **Save as type**, select **Adobe Portable Document Format**.
3. Select **Save as 3D PDF**.
4. Click **Options**.

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Accuracy - Maximum, High, Medium, or Low | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.sw3DPDFAccuracy) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.sw3DPDFAccuracy, sw3DPDFAccuracy_e.< Value >) | See sw3DPDFAccuracy_e for valid options |  |
| Use lossy compression on tessellation | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.sw3DPDFCompressLossyTessellation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.sw3DPDFCompressLossyTessellation, < OnFlag >) | Boolean value | Specifies whether to use lossy compression on tessellation |
