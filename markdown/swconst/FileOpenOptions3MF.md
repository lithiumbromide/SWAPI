---
title: "System Options > Import > 3MF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptions3MF.htm"
---

# System Options > Import > 3MF

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > 3MF**.

- or -

1. Select **File > Open**.
2. In **Files of type**, select **3D Manufacturing Format**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Import as - Graphics body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Graphics) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Graphics |  |
| Import as - Solid body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Solid) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Solid |  |
| Import as - Surface body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Surface) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Surface |  |
| Mesh body options - Create mesh bodies bounded by single faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh, < OnFlag >) | Boolean value | Valid only when importing as Solid body or Surface body, specifies whether to create mesh bodies bounded by single faces |
| Mesh body options - Group facets into faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportSegmented) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportSegmented, < OnFlag >) | Boolean value | Valid only if Create mesh bodies bounded by single faces is selected, specified whether to group facets into faces |
| Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlUnits, swLengthUnit_e.< Value >) | Valid options from swLengthUnit_e : 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
