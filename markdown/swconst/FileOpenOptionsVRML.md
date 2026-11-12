---
title: "System Options > Import > VRML or 3MF"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsVRML.htm"
---

# System Options > Import > VRML or 3MF

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > VRML** or **3MF**.

- or -

1. Select **File > Open**.
2. In **Files of type**, select **VRML** or **3D Manufacturing Format**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Import as - Graphics body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Graphics) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Graphics |  |
| Import as - Solid body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Solid) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Solid |  |
| Import as - Surface body | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Surface) | swImportStlVrmlModelType_e .swImportStlVrmlModelType_Surface |  |
| Unit | ISldWorks::GetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlUnits) ISldWorks::SetUserPreferenceIntegerValue (swUserPerferenceIntegerValue_e.swImportStlVrmlUnits, swLengthUnit_e.< Value >) | Valid options from swLengthUnit_e : 0 = swMM (millimeters) 1 = swCM (centimeters) 2 = swMETER 3 = swINCHES 4 = swFEET |  |
| Import texture information | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportStlVrmlTextureInformation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportStlVrmlTextureInformation, < OnFlag >) | Boolean value |  |
