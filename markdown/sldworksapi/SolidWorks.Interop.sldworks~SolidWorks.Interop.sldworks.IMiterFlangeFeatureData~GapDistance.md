---
title: "GapDistance Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "GapDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~GapDistance.html"
---

# GapDistance Property (IMiterFlangeFeatureData)

Gets or sets the gap distance of the tear for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

Distance in meters between edges in the miter flange

## VBA Syntax

See [MiterFlangeFeatureData::GapDistance](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~GapDistance.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
