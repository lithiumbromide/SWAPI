---
title: "GetFromEntity Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "GetFromEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFromEntity.html"
---

# GetFromEntity Method (IMoveFaceFeatureData)

Gets the entity from which the face of the Move Face feature is translated.

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
Dim instance As IMoveFaceFeatureData
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

- `FromEntity`: [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), or [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html) from which the face of the Move Face feature is translated
- `Type`: Type of end condition as defined in [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [MoveFaceFeatureData::GetFromEntity](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~GetFromEntity.html).

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::SetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.html)
[IMoveFaceFeatureData::GetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)
[IMoveFaceFeatureData::SetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.html)
[IMoveFaceFeatureData::EndCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
