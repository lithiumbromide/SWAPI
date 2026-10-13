---
title: "Get DimXpert Tolerance4 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance4_Example_VBNET.htm"
---

# Get DimXpert Tolerance4 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Angle-between dimension tolerance

* Chamfer dimension tolerance

* Line Profile geometric tolerance

* Straightness geometric tolerance

```vb
'----------------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' 3. Create the chamfer dimension tolerance:
'    a. Click Auto-Dimension Scheme on the DimXpert toolbar.
'    b. Ensure that the Chamfer feature filter is selected.
'    c. Click the green arrow to accept the settings.
'    d. Observe ChamferDepth1 and ChamferDepth2 in the DimXpert tree.
' 4. Create angle-between dimension tolerance:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Click a face of the part.
'    c. Click a face perpendicular to the face
'       selected in step 2 (not the chamfer).
'    d. Click outside the part to place the annotation.
'    e. Find the following in the DimXpert tree: AngleBetween1.
' 5. Create line profile and straightness geometric tolerances:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.   Select Straightness from the Symbol dropdown
'            list.
'       ii.  In second row, select Profile of Line from
'            the Symbol dropdown list.
'       iii. Type 0.25 in Tolerance1.
'       iv.  Click the top face of the part.
'       v.   Click outside the part to place the
'            annotation.
'       vi.  Click OK to close the Geometric Tolerance
'            Properties dialog.
'    b. Observe the following DimXpert annotations:
'       LineProfile1 and Straightness1.
' 6. Close the part, saving it to another name.
'    NOTE: Because these parts are used in a SOLIDWORKS
'          online tutorial, do not save any changes to
'          the original file name.
' 7. Read how to load and run Code_Example_VBNET with this part.
'----------------------------------------------------------------------------
```
