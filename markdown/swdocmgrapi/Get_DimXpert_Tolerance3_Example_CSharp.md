---
title: "Get DimXpert Tolerance3 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance3_Example_CSharp.htm"
---

# Get DimXpert Tolerance3 Example (C#)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Position geometric tolerance

* Orientation (Perpendicularity) geometric tolerance

```vb
 //-----------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\cover_position.sldprt.
// 2. Click Geometric Tolerance on the DimXpert toolbar.
//    In the Geometric Tolerance Properties dialog:
//    a. Select Position from the Symbol dropdown
//       list in the first row.
//    b. Type A in Primary, B in Secondary, and C in Tertiary.
//    c. In second row (lower tier), select Position from the
//       Symbol dropdown list.
//    d. Type 0.25 in Tolerance1.
//    e. Type A in Primary.
//    f. Select the Composite frame check box.
//    g. Click the circular face of the boss.
//    h. Click outside the part to place the annotation.
//    i. Click OK to close the Geometric Tolerance
//       Properties dialog.
// 3. Observe the following DimXpert annotations:
//    Position1 and Perpendicularity1.
// 4. Close the part, saving it to another name.
//    NOTE: Because this part is used in a SOLIDWORKS online
//          tutorial, do not save any changes to the original file name.
// 5. Read how to load and run Code_Example_CSharp with this part.
 //------------------------------------------------------------------------------
```
