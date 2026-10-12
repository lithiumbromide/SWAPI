---
title: "SetFromEntity Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "SetFromEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.html"
---

# SetFromEntity Method (IMoveFaceFeatureData)

Sets the entity from which the face of the Move Face feature is translated.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFromEntity( _
   ByVal FromEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
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

- `FromEntity`: [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), or [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html) from which the face of the Move Face feature is translated

## VBA Syntax

See [MoveFaceFeatureData::SetFromEntity](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~SetFromEntity.html).

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::SetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.html)
[IMoveFaceFeatureData::GetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)
[IMoveFaceFeatureData::SetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.html)
[IMoveFaceFeatureData::EndCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
