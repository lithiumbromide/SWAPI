---
title: "PositionType Property (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "PositionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~PositionType.html"
---

# PositionType Property (ISketchedBendFeatureData)

Gets or sets the bend position of this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As System.Integer

instance.PositionType = value

value = instance.PositionType
```

### C#

```csharp
System.int PositionType {get; set;}
```

### C++/CLI

```cpp
property System.int PositionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend position as defined in [swFlangePositionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html)

## VBA Syntax

See [SketchedBendFeatureData::PositionType](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~PositionType.html).

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
