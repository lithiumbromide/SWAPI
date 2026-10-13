---
title: "FlipSideToCut Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "FlipSideToCut"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FlipSideToCut.html"
---

# FlipSideToCut Property (IExtrudeFeatureData2)

Gets or sets whether to flip the side to cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipSideToCut As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean

instance.FlipSideToCut = value

value = instance.FlipSideToCut
```

### C#

```csharp
System.bool FlipSideToCut {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipSideToCut {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True flips the side to cut, false does not

## VBA Syntax

See [ExtrudeFeatureData2::FlipSideToCut](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~FlipSideToCut.html).

## Remarks

This property is relevant only for cut features.

If the sketch is open, then the first edge in the array returned by [ISketch::GetContourEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetContourEdges.html) and [ISketch::IGetControuEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetContourEdges.html) is cut.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
