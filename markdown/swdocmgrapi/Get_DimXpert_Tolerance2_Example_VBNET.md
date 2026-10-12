---
title: "Get DimXpert Tolerance2 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance2_Example_VBNET.htm"
---

# Get DimXpert Tolerance2 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Distance-between dimension tolerance

* Composite distance-between dimension tolerance

* Symmetry geometric tolerance

* Radius dimension tolerance

* Diameter dimension tolerance

```vb
 '--------------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Open the DimXpert toolbar from View > toolbars
'    (select the first instance of toolbars on the View menu).
' 3. Create a distance-between dimension tolerance:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Click the left-front face of the block.
'    c. Click Create Compound Plane on the DimXpert
'       pop-up toolbar.
'    d. Click the right front face of the block.
'    e. Click the green check mark to accept the faces.
'    f. Click the back face of the block to complete the
'       location dimension.
'    g. Click outside the part to position the location dimension.
'    h. Click ESC to end dimensioning.
'    i. Observe the following DimXpert annotation:  DistanceBetween1.
' 4. Create composite distance-between and radius dimension tolerances:
'    a. Click Auto Dimension Scheme on the DimXpert toolbar.
'    b. Select Part type: Prismatic.
'    c. Select Tolerance type: Plus and Minus
'    d. Click in the Primary Datum field; select face in front of right hole.
'    e. Click in the Secondary Datum field; select top face of block.
'    f. Select all feature filters.
'    g. Click the green check mark to accept the DimXpert settings.
'    h. Observe the following DimXpert annotations:
'       Diameter1, DistanceBetween5, and Radius1.
' 5. Create a symmetry geometric tolerance:
'    a. Click Datum on the DimXpert toolbar.
'    b. Click the face in front of the left hole and click
'       outside the part to place Datum A.
'    c. Click the green check mark to finish the Datum
'       definition.
'    d. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.   Select Symmetry from the Symbol dropdown list.
'       ii.  Type A for the Primary Datum.
'       iii. Click the face in front of the right hole.
'       iv.  Click outside the part to place the annotation.
'       v.   Click OK to close the Geometric Tolerance
'            Properties dialog.
'    e. Observe the following DimXpert annotation: Symmetry1.
' 6. Close the part, saving it to another name.
'    NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original file name.
' 7. Read how to load and run Code_Example_VBNET with this part.
 '------------------------------------------------------------------------------
```
