---
title: "GetFromEntity Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetFromEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity.html"
---

# GetFromEntity Method (IExtrudeFeatureData2)

Gets the entity and its type from which the extrusion was created.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetFromEntity( _
   ByRef FromEntity As System.Object, _
   ByRef Type As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim FromEntity As System.Object
Dim Type As System.Integer

instance.GetFromEntity(FromEntity, Type)
```

### C#

```csharp
void GetFromEntity(
   out System.object FromEntity,
   out System.int Type
)
```

### C++/CLI

```cpp
void GetFromEntity(
   [Out] System.Object^ FromEntity,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromEntity`: Entity from which the extrusion was created:

  - Surface
  - Face
  - Plane
  - Vertex
  - Sketch point
- `Type`: Type of entity from which to create the extrusion as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [ExtrudeFeatureData2::GetFromEntity](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetFromEntity.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::FromType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.html)
[IExtrudeFeatureData2::SetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
