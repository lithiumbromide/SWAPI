---
title: "Get DimXpert Tolerance1 Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Tolerance1_Example_CSharp.htm"
---

# Get DimXpert Tolerance1 Example (C#)

This example builds a part to demonstrate usage of the SOLIDWORKS Document Manager API for the following DimXpert annotations:

* Circularity geometric tolerance

* Cylindricity geometric tolerance

* Countersink angle dimension tolerance

* Countersink diameter dimension tolerance

* Flatness geometric tolerance

* Surface profile geometric tolerance

* Length dimension tolerance

* Width dimension tolerance

```vb
 //--------------------------------------------------------------------------
// 1. Open public_documents\samples\tutorial\api\cover_with_geometric_tolerances.sldprt.
// 2. Click Auto Dimension Scheme on the DimXpert toolbar and
//    ensure that all feature filters are selected.
//    Click the green check mark to accept the settings.
// 3. Click Geometric Tolerance on the DimXpert toolbar.
//    In the Geometric Tolerance Properties dialog:
//    a. Select Cylindricity from the Symbol dropdown in the first row.
//    b. In the second row, select Profile of Surface from the
//       Symbol dropdown list and type a tolerance of 0.5 next to it.
//    c. Click the outer-base cylinder and click again outside
//       the part to place the annotation.
//    d. Click OK to close the Geometric Tolerance Properties dialog.
// 4. In the DimXpertManager tab of the Management Panel, expand all of
//    the nodes in the tree.
// 5. Observe the following DimXpert annotations:  Flatness1, Circularity1,
//    Diameter1,  CounterSinkAngle1, CounterSinkDiameter1, Cylindricity1,
//    Surface Profile1, Length1, Width1
// 6. Close the part, saving it to another name.
//    NOTE: Because this part is used in a SOLIDWORKS online tutorial,
//          do not save any changes to the original file name.
// 7. Read how to load and run Code_Example_CSharp with this part.
 //-------------------------------------------------------------------------
```
