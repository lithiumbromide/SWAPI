---
title: "System Options > Import > Inventor/Catia V5/Creo/NX/Solid Edge"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsInventorCatiaCreoNXSE.htm"
---

# System Options > Import > Inventor/Catia V5/Creo/NX/Solid Edge

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > Inventor/Catia V5/Creo/NX/Solid Edge**.

- or -

1. Click **File > Open**.
2. In **Files of type**, select **Inventor** (**Part** or **Assembly**), **Catia V5**, **ProE/Creo** (**Part** or **Assembly**), **Unigraphics/NX**, or **Solid Edge** (**Part** or **Assembly**).
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Entities to Read From 3rd Party CAD Files - Solid Body | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSolidBody) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSolidBody, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Surface Body | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSurfaceBody) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportSurfaceBody, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Reference Plane | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportReferencePlane) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportReferencePlane, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Reference Axis | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportReferenceAxis) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportReferenceAxis, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Unconsumed Sketch(es) and Curves | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportUnconsumedSketchesAndCurves) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportUnconsumedSketchesAndCurves, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Custom Properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportCustomProperties) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportCustomProperties, < OnFlag >) | Boolean value |  |
| Entities to Read From 3rd Party CAD Files - Material Properties | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportMaterialProperties) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportMaterialProperties, < OnFlag >) | Boolean value |  |
| Options - Dissolve top level assembly on open (Not supported in SOLIDWORKS Design connected to the 3DEXPERIENCE platform) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportDissolveTopLevelAssemblyOnOpen) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportDissolveTopLevelAssemblyOnOpen, < OnFlag >) | Boolean value |  |
| Options - Ignore Hidden Entities | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIgnoreHiddenEntities) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportIgnoreHiddenEntities, < OnFlag >) | Boolean value |  |
| Options - Import tool bodies from UG NX | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportToolBodiesFromUGNX) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportToolBodiesFromUGNX, < OnFlag >) | Boolean value |  |
