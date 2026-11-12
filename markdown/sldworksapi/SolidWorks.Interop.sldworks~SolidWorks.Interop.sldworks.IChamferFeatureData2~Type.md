---
title: "Type Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Type.html"
---

# Type Property (IChamferFeatureData2)

Gets or sets the type of chamfer feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of chamfer as defined in [swChamferType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swChamferType_e.html)

## VBA Syntax

See [ChamferFeatureData2::Type](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~Type.html).

## Examples

[Get Chamfer Distances (VB.NET)](Get_Chamfer_Distances_Example_VBNET.htm)
[Get Chamfer Distances (C#)](Get_Chamfer_Distances_Example_CSharp.htm)
[Get Chamfer Distances (VBA)](Get_Chamfer_Distances_Example_VB.htm)

## Remarks

Both swChamferType_e.swChamferAngleDistance and swChamferType_e.swChamferDistanceDistance are edge chamfers. This means that all measurements are from edges. An angle-distance chamfer requires an angle and a distance; a distance-distance chamfer requires two distances, one for each side of the chamfered edge.

A swChamferType_e.swChamferVertex chamfer only works on a vertex with three adjacent edges of the same convexity. A vertex chamfer requires three distances along three adjacent edges. For non-linear edges, this value is an arc length value; it is not a chordal value. See [IVertex::EnumEdgesOriented](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~EnumEdgesOriented.html) to determine the edge order used by this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
