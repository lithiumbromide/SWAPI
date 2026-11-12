---
title: "Collapse Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "Collapse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Collapse.html"
---

# Collapse Method (IBomTableAnnotation)

Collapses the specified item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Collapse( _
   ByVal CollapseType As System.Integer, _
   ByVal Index As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim CollapseType As System.Integer
Dim Index As System.Integer

instance.Collapse(CollapseType, Index)
```

### C#

```csharp
void Collapse(
   System.int CollapseType,
   System.int Index
)
```

### C++/CLI

```cpp
void Collapse(
   System.int CollapseType,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CollapseType`: Type of item to collapse as defined in [swBOMTableObjectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMTableObjectType_e.html) (see **Remarks**)
- `Index`: Row index; valid only if CollapseType is swBOMTableObjectType_e.swBOMTableObjectType_RowIndex

## VBA Syntax

See [BomTableAnnotation::Collapse](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~Collapse.html).

## Examples

[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (VBA)](Dissolve_Subassembly_in_a_BOM_Table_Example_VB.htm)
[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (VB.NET)](Dissolve_Subassembly_in_a_BOM_Table_Example_VBNET.htm)
[Expand, Collapse, and Dissolve a Subassembly in a BOM Table (C#)](Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm)

## Remarks

If CollapseType is swBOMTableObjectType_e.swBOMTableObjectType_CutList, then all cut lists in the table collapse.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::Expand Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Expand.html)
[IBomTableAnnotation::Dissolve Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Dissolve.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
