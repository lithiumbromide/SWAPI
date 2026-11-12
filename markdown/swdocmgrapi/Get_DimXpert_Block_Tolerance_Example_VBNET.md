---
title: "Get DimXpert Block Tolerance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_DimXpert_Block_Tolerance_Example_VBNET.htm"
---

# Get DimXpert Block Tolerance Example (VB.NET)

This example demonstrates how to use the SOLIDWORKS Document Manager API to acquire the following block tolerance values:

* ISO

* ASME

```vb
'----------------------------------------------------------------------------
 ' ISO:
 ' 1. Open public_documents\samples\tutorial\dimxpert\shaft.sldprt.
 ' 2. Open the DimXpert toolbar from View > Toolbars
 '    (select the first instance of Toolbars on the View menu).
 ' 3. Click Auto Dimension Scheme in the DimXpert toolbar.
 ' 4. Click the green check mark to accept all settings.
 ' 5. Close the part, saving it to another name.
 '    NOTE:  Because this part is used in SOLIDWORKS tutorials,
 '           do not save changes to the original file name.
 ' 6. Read the instructions to load and run Code_Example_VBNET
 '    with this part.
 ' 7. Inspect the Immediate Window to see the ISO code for the part.
 '
 ' ASME:
 ' 1. Open:
 ' public_documents\samples\tutorial\dimxpert\cover_with_geometric_tolerances.sldprt
 '  2. Close the part, saving it to another name.
 '     NOTE:  Because this part is used in SOLIDWORKS tutorials,
 '           do not save changes to the original file name.
 ' 3. Read the instructions to load and run Code_Example_VBNET
 '    with this part.
 ' 4. Inspect the Immediate Window to see the ASME block tolerance
 '    values for the part.
 '----------------------------------------------------------------------------
```
