---
title: "OffsetDistance Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~OffsetDistance.html"
---

# OffsetDistance Property (IMoveFaceFeatureData)

Gets or sets the offset distance of this translated Move Face feature that has an end condition of **Offset From Surface**.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Double

instance.OffsetDistance = value

value = instance.OffsetDistance
```

### C#

```csharp
System.double OffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset distance of this translated Move Face feature that has an end condition of **Offset From Surface** (see **Remarks**)

## VBA Syntax

See [MoveFaceFeatureData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~OffsetDistance.html).

## Examples

[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)
[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)

## Remarks

For all other end conditions, use [IMoveFaceFeatureData::Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Distance.html) to get or set the offset distance of a translated Move Face feature.

To find out the type of:

- Move Face feature, use [IMoveFaceFeatureData::MoveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.html).
- end condition, use [IMoveFaceFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.html).

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
