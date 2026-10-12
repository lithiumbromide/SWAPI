---
title: "PickPoints Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "PickPoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~PickPoints.html"
---

# PickPoints Property (ILoftFeatureData)

Gets or sets the pick points of a loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PickPoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Object

instance.PickPoints = value

value = instance.PickPoints
```

### C#

```csharp
System.object PickPoints {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PickPoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the pick points that contain arrays of coordinates of the pick points of this loft feature

## VBA Syntax

See [LoftFeatureData::PickPoints](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~PickPoints.html).

## Examples

[Get and Set Loft's Pick Points (VB.NET)](Get_Loft's_Pick_Points_Example_VBNET.htm)
[Get and Set Loft's Pick Points (C#)](Get_Loft's_Pick_Points_Example_CSharp.htm)

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
