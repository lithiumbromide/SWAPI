---
title: "GapDistance Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "GapDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GapDistance.html"
---

# GapDistance Property (IEdgeFlangeFeatureData)

Gets or sets the gap distance of the tear for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.GapDistance = value

value = instance.GapDistance
```

### C#

```csharp
System.double GapDistance {get; set;}
```

### C++/CLI

```cpp
property System.double GapDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters between the edges in the flange; default value is 0.001 m

## VBA Syntax

See [EdgeFlangeFeatureData::GapDistance](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~GapDistance.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
