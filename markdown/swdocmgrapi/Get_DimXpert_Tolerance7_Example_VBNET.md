---
title: "Get DimXpert Tolerance7 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance7_Example_VBNET.htm"
---

# Get DimXpert Tolerance7 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for a DimXpert line profile geometric tolerance annotation.

```vb
 '--------------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\api\plate_tolstatus.sldprt.
' 2. Open the DimXpert toolbar from View > Toolbars
'    (select the first instance of Toolbars on the View menu).
' 3. Click Datum on the DimXpert toolbar and create
'    Datum A somewhere on the part.
' 4. Create the line profile geometric tolerance:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'          i.    Select Line Profile from the Symbol dropdown in
'                the first row.
'          ii.   Type A in Primary of the first row.
'          iii.  In the second row, select Line Profile from the Symbol
'                dropdown list.
'          iv.   In the second row, type a tolerance in Tolerance 1.
'          v.    In the second row, type A in Primary.
'          vi.   Select Composite frame.
'          vii.  Click the inner face of the hole.
'          viii. Click outside the part to place the annotation.
'          ix.   Click OK to close the Geometric Tolerance
'                Properties dialog.
'    b. Observe LineProfile1 and LineProfile2 under SimpleHole1
'       in the DimXpert tree.
' 5. Close the part, saving it to another name.
'    NOTE: Because these parts are used in a SOLIDWORKS online
'          tutorial, do not save any changes to the original
'          file name.
' 6. Read how to load and run Code_Example_VBNET with this part.
 '-----------------------------------------------------------------------------
```
