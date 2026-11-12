---
title: "Get DimXpert Tolerance6 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance6_Example_VBNET.htm"
---

# Get DimXpert Tolerance6 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Surface profile geometric tolerance

* Tangency geometric tolerance

```vb
 '-------------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\cosmosxpress\aw_anchor_plate.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' 3. Create a surface profile tolerance:
'    a. Click Datum on the DimXpert toolbar.
'    b. Click a top face of the part.
'    c. Click outside the part to place Datum A.
'    d. Click a back face of the part.
'    e. Click outside the part to place Datum B.
'    f. Click a side face of the part.
'    g. Click outside the part to place Datum C.
'    h. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.    Select Profile of Surface from the Symbol dropdown list.
'       ii.   Type 50 in Tolerance 1.
'       iii.  Type A in the Primary box and C in the
'             Secondary box.
'       iv.   In the second row, select Profile of Surface from
'             the Symbol dropdown list.
'       v.    In the second row, type 50 in Tolerance 1.
'       vi.   In the second row, type A in the Primary box.
'       vii.  Select the Composite frame check box.
'       viii. Click the front curve of the hook.
'       ix.   Click outside the part to place the annotation.
'       x.    Click OK to close the Geometric Tolerance
'             Properties dialog.
'    i. In the DimXpertManager tab of the Management Panel,
'       expand Cylinder1.
'    j. Observe the following DimXpert annotations:
'       Surface Profile1 and Surface Profile2
' 4. Create tangency tolerances:
'    a. Click Auto Dimension Scheme on the DimXpert toolbar.
'    b. Select all feature filters.
'    c. Click the green check mark to accept the settings.
'    d. Observe several tangency tolerance annotations.
' 5. Close the part, saving it to another name.
'    NOTE: Because this part is used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' 6. Read how to load and run Code_Example_VBNET with this part.
 ' --------------------------------------------------------------------------
```
