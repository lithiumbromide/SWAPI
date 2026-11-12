---
title: "System Options > Import > STL/OBJ/OFF/PLY/PLY2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsSTLVRML.htm"
---

# System Options > Import > STL/OBJ/OFF/PLY/PLY2

To display the dialog:

Click **Tools > Options > System Options > Import > STL/OBJ/OFF/PLY/PLY2** in **File Format**.

- or -

1. Click **File > Open**.
2. In **Files of type**, select **Mesh Files**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Import as - Graphics body | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Graphics) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Graphics |  |
| Import as - Solid body | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Solid) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Solid |  |
| Import as - Surface body | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Surface) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Surface |  |
| Mesh body options - Create mesh bodies bounded by single faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh, < OnFlag >) | Boolean value | Valid only when importing as Solid body or Surface body, specifies whether to create mesh bodies bounded by single faces |
| Mesh body options - Group facets into faces | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIVrmlStlImportSegmented) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIVrmlStlImportSegmented, < OnFlag >) | Boolean value | Valid only if Create mesh bodies bounded by single faces is selected, specified whether to group facets into faces |
| Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swImportStlVrmlUnits, swLengthUnit_e.< Value >) | Valid options from swLengthUnit_e : 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
