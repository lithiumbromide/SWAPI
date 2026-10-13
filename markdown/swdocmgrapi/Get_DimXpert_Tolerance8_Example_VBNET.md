---
title: "Get DimXpert Tolerance8 Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance8_Example_VBNET.htm"
---

# Get DimXpert Tolerance8 Example (VB.NET)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Circular runout geometric tolerance

* Total runout geometric tolerance

* Angularity geometric tolerance

* Parallelism geometric tolerance

```vb
 '-----------------------------------------------------------------------------
' 1. Open public_documents\samples\tutorial\api\cover_datum.sldprt.
' 2. Click Datum on the DimXpert toolbar and place
'    Datum A inside the hole.
' 3. Create the circular runout geometric tolerance:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.  Select Circular Runout from the Symbol dropdown
'           list in the first row.
'       ii.  In the Primary field, type A.
'       iii. Click the outer cylinder of the part and click
'            again outside the part to place
'            the annotation.
'       iv.  Click OK to close the Geometric Tolerance
'            Properties dialog.
'    b. Observe CircularRunout1 under Cylinder1 in the
'       DimXpert tree.
' 4. Create the total runout geometric tolerance:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.   Select Total Runout from the Symbol dropdown
'            list in the first row.
'       ii.  In the Primary field, type A.
'       iii. Click the boss of the part and click again
'            outside the part to place
'            the annotation.
'       iv.  Click OK to close the Geometric Tolerance
'            Properties dialog.
'    b. Observe TotalRunout1 under Boss1 in the DimXpert
'       tree.
' 5. Create the angularity geometric tolerance:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.   Select Angularity from the Symbol dropdown
'            in the first row.
'       ii.  In the Primary field, type A.
'        iii. Click a face of the notch and click again
'            outside the part to place the annotation.
'       iv.  Click OK to close the Geometric Tolerance
'            Properties dialog.
'    b. Observe Angularity1 under Notch1 in the DimXpert
'       tree.
' 6. Create the parallelism geometric tolerance:
'    a. Click Geometric Tolerance on the DimXpert toolbar.
'       In the Geometric Tolerance Properties dialog:
'       i.   Select Parallel from the Symbol dropdown
'            in the first row.
'       ii.  In the Primary field, type A.
'       iii. Click the boss of the part and click again
'            outside the part to place the annotation.
'       iv.  Click OK to close the Geometric Tolerance
'            Properties dialog.
'    b. Observe Parallelism1 under Boss1 in the DimXpert tree.
' 7. Close the part, saving it to another name.
'     NOTE: Because this part is used in a SOLIDWORKS online
'           tutorial, do not save any changes to the original
'           file name.
' 8. Read how to load and run Code_Example_VBNET with this part.
 '-----------------------------------------------------------------------------
```
