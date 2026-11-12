---
title: "EndCondition Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html"
---

# EndCondition Property (IMoveFaceFeatureData)

Gets the end condition for this translated Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Integer

instance.EndCondition = value

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition as defined in [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [MoveFaceFeatureData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~EndCondition.html).

## Examples

[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)
[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::GetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.html)
[IMoveFaceFeatureData::SetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.html)
[IMoveFaceFeatureData::Distance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Distance.html)
[IMoveFaceFeatureData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~OffsetDistance.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
