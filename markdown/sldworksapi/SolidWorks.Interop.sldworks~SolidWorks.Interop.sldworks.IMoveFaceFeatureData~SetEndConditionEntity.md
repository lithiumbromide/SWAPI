---
title: "SetEndConditionEntity Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "SetEndConditionEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.html"
---

# SetEndConditionEntity Method (IMoveFaceFeatureData)

Sets the entity to which the face of the Move Face feature is translated.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEndConditionEntity( _
   ByVal EndEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim EndEntity As System.Object

instance.SetEndConditionEntity(EndEntity)
```

### C#

```csharp
void SetEndConditionEntity(
   System.object EndEntity
)
```

### C++/CLI

```cpp
void SetEndConditionEntity(
   System.Object^ EndEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EndEntity`: [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) to which the face of the Move Face feature is translated (see **Remarks**)

## VBA Syntax

See [MoveFaceFeatureData::SetEndConditionEntity](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~SetEndConditionEntity.html).

## Remarks

The type of entity depends on the type of [end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html).

| End condition | Type of entity |
| --- | --- |
| Up To Vertex | Vertex |
| Up To Surface or Offset From Surface | Face, plane, or surface |
| Up To Body | Body or surface |

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::GetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)
[IMoveFaceFeatureData::GetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFromEntity.html)
[IMoveFaceFeatureData::SetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
