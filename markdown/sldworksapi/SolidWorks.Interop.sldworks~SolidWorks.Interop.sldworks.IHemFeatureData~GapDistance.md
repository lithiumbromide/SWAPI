---
title: "GapDistance Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "GapDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~GapDistance.html"
---

# GapDistance Property (IHemFeatureData)

Gets or sets the hem gap distance for open hems only.

## Syntax

### Visual Basic (Declaration)

```vb
Property GapDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
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

Gap distance

## VBA Syntax

See [HemFeatureData::GapDistance](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~GapDistance.html).

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
