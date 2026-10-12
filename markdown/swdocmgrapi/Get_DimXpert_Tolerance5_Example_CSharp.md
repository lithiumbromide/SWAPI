---
title: "Get DimXpert Tolerance5 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance5_Example_CSharp.htm"
---

# Get DimXpert Tolerance5 Example (C#)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for a DimXpert concentricity geometric tolerance annotation.

```vb
 //--------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\cover_with_dimensions.sldprt.
// 2. Open the DimXpert toolbar from View > Toolbars
//    (select the first instance of Toolbars on the View menu).
// 3. Create concentricity tolerance:
//    a. Click Datum on the DimXpert toolbar.
//    b. Click Boss1 (front extrusion).
//    c. Click outside the part to place the annotation.
//    d. Click the green check mark to accept Datum A.
//    e. Click Geometric Tolerance on the DimXpert toolbar.
//       In the Geometric Tolerance Properties dialog:
//            i.    Select Concentricity from the Symbol dropdown list.
//            ii.   Click inside the Tolerance 1 field.
//             iii.  Click Diameter on the toolbar
//                  at the top of the dialog.
//            iv.   Type A in the Primary field.
//            v.    Click the inside face of Simple Hole2.
//            vi.   Click outside the part to place the annotation.
//            vii.  Click OK to close the Geometric Tolerance Properties dialog.
//    f. In the DimXpertManager tab of the Management Panel,
//       expand Simple Hole2.
//    g. Observe the following Dimxpert annotation: Concentricity1.
// 4. Close the part, saving it to another name.
//    NOTE: Because this part is used in a SOLIDWORKS online tutorial,
//          do not save any changes to the original file name.
// 5. Read how to load and run Code_Example_CSharp with this part.
 //-----------------------------------------------------------------------
```
