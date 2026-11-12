---
title: "GetEntitiesWeldFrom Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "GetEntitiesWeldFrom"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.html"
---

# GetEntitiesWeldFrom Method (ICosmeticWeldBeadFeatureData)

Gets the weld-from entity type and weld-from entities for this cosmetic weld bead, which was created using weld geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesWeldFrom( _
   ByRef EntType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim EntType As System.Integer
Dim value As System.Object

value = instance.GetEntitiesWeldFrom(EntType)
```

### C#

```csharp
System.object GetEntitiesWeldFrom(
   out System.int EntType
)
```

### C++/CLI

```cpp
System.Object^ GetEntitiesWeldFrom(
   [Out] System.int EntType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntType`: Weld-from entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html); i.e., either swSelFACES or swSelEDGES

### Return Value

Array of weld-from entities of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.html).

## Examples

[Insert Cosmetic Weld Bead Using Geometric Entities (C#)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_CSharp.htm)
[Insert Cosmetic Weld Bead Using Geometric Entities (VB.NET)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VBNET.htm)
[Insert Cosmetic Weld Bead Using Geometric Entities (VBA)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VB.htm)

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.html)
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.html)
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.html)

## Availability

SOLIDWORKS 2105 FCS, Revision Number 23.0
