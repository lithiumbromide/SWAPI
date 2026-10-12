---
title: "Distance Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Distance.html"
---

# Distance Property (IMoveFaceFeatureData)

Gets or sets the offset distance of this offset or translated Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset distance of this offset or translated Move Face feature (see **Remarks**)

## VBA Syntax

See [MoveFaceFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~Distance.html).

## Examples

[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)
[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)

## Remarks

To find out whether the Move Face feature was offset or translated, use [IMoveFaceFeatureData::MoveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.html).

If setting the offset distance of a translated Move Face feature that has an [end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html) of **Offset From Surface**, then use [IMoveFaceFeatureData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~OffsetDistance.html). For all other end conditions, use IMoveFaceFeatureData::Distance to set the offset distance.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
