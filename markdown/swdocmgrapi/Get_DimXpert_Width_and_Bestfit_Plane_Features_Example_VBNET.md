---
title: "Get DimXpert Compound Width and Best Fit Plane Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Width_and_Bestfit_Plane_Features_Example_VBNET.htm"
---

# Get DimXpert Compound Width and Best Fit Plane Features Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert features:

* Width

* Best fit plane

```vb
 '----------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' 3. Create the DimXpert best fit plane feature:
'    a. Click Location Dimension on the DimXpert toolbar.
'    b. Select the left-front face of the block.
'    c. Click Compound Plane on the DimXpert pop-up
'       toolbar.
'    d. Select the right front face of the block.
'    e. Click the green check mark on the DimXpert pop-up toolbar.
'    f. Select the back face of the block.
'    g. Click outside the part to place the location dimension
'       annotation.
'    h. Observe the best fit plane DimXpert feature on the
'       DimXpertManager tab.
' 4. Create the DimXpert width feature:
'    a. Click Size Dimension on the DimXpert toolbar.
'    b. Select a front face of the block.
'    c. Click Width on the DimXpert pop-up toolbar.
'    d. Select the back face of the block.
'    e. Click the green check mark on the DimXpert pop-up toolbar.
'    f. Click outside the part to place the size dimension annotation.
' 5. Observe the following DimXpert feature on the DimXpertManager
'    tab:  Width1.
' 6. Close the part, saving it to another name.
'    NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' 7. Read how to load and run Code_Example_VBNET with this part.
 '----------------------------------------------------------------------
```
