---
title: "Expand Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "Expand"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.html"
---

# Expand Method (IBomTableAnnotation)

Expands the specified item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Expand( _
   ByVal ExpandType As System.Integer, _
   ByVal Index As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim ExpandType As System.Integer
Dim Index As System.Integer

instance.Expand(ExpandType, Index)
```

### C#

```csharp
void Expand(
   System.int ExpandType,
   System.int Index
)
```

### C++/CLI

```cpp
void Expand(
   System.int ExpandType,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExpandType`: Type of item to expand as defined in [swBOMTableObjectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMTableObjectType_e.html)
- `Index`: Row index; valid only if ExpandType is swBOMTableObjectType_e.swBOMTableObjectType_RowIndex

## VBA Syntax

See [BomTableAnnotation::Expand](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~Expand.html).

## Examples

[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)
[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)
[Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

## Remarks

If ExpandType is swBOMTableObjectType_e.swBOMTableObjectType_CutList, then all cut lists in the table expand.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::Collapse Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.html)
[IBomTableAnnotation::Dissolve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
