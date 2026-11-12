---
title: "SetFromEntity Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetFromEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity.html"
---

# SetFromEntity Method (IExtrudeFeatureData2)

Sets the entity from which to create an extrusion.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFromEntity( _
   ByVal FromEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim FromEntity As System.Object

instance.SetFromEntity(FromEntity)
```

### C#

```csharp
void SetFromEntity(
   System.object FromEntity
)
```

### C++/CLI

```cpp
void SetFromEntity(
   System.Object^ FromEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromEntity`: Entity from which to create the extrusion:

  - Surface
  - Face
  - Plane
  - Vertex
  - Sketch point

## VBA Syntax

See [ExtrudeFeatureData2::SetFromEntity](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetFromEntity.html).

## Remarks

You must also set the type of entity using [IExtrudeFeatureData2::FromType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~FromType.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
