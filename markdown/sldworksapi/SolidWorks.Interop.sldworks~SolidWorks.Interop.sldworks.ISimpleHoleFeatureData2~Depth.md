---
title: "Depth Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "Depth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Depth.html"
---

# Depth Property (ISimpleHoleFeatureData2)

Gets or sets the depth of this simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Depth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Double

instance.Depth = value

value = instance.Depth
```

### C#

```csharp
System.double Depth {get; set;}
```

### C++/CLI

```cpp
property System.double Depth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole depth

## VBA Syntax

See [SimpleHoleFeatureData2::Depth](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~Depth.html).

## Remarks

This property only supports getting the depth of a blind hole. To get the depth of holes with other types of end conditions, you could:

- use [IExtrudeFeatureData2::GetDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetDepth.html) to get the length of the extrusion.
- analyze the curves and edges of the hole to get the depth or thickness of it at a specific point.
- use [ISimpleHoleFeatureData2::SurfaceOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~SurfaceOffset.html) for a hole with a depth that is offset from the surface.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
