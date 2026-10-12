---
title: "EdgeChamferAngle Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "EdgeChamferAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~EdgeChamferAngle.html"
---

# EdgeChamferAngle Property (IChamferFeatureData2)

Gets or sets the angle on the edge of the chamfer feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EdgeChamferAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Double

instance.EdgeChamferAngle = value

value = instance.EdgeChamferAngle
```

### C#

```csharp
System.double EdgeChamferAngle {get; set;}
```

### C++/CLI

```cpp
property System.double EdgeChamferAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Chamfer angle of the edge of the chamfer feature

## VBA Syntax

See [ChamferFeatureData2::EdgeChamferAngle](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~EdgeChamferAngle.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## Remarks

This method is relevant only for an angle-distance type of chamfer.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Type.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
