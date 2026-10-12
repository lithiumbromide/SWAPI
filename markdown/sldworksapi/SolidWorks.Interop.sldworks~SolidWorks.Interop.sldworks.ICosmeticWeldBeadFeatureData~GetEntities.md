---
title: "GetEntities Method (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "GetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntities.html"
---

# GetEntities Method (ICosmeticWeldBeadFeatureData)

Obsolete. Superseded by [ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.html) and [ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntities( _
   ByRef EntType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim EntType As System.Integer
Dim value As System.Object

value = instance.GetEntities(EntType)
```

### C#

```csharp
System.object GetEntities(
   out System.int EntType
)
```

### C++/CLI

```cpp
System.Object^ GetEntities(
   [Out] System.int EntType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntType`: Entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) and [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::GetEntities](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~GetEntities.html).

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::SetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntities.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
