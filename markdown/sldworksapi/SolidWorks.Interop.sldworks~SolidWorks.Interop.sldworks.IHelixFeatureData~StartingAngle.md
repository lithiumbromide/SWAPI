---
title: "StartingAngle Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "StartingAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~StartingAngle.html"
---

# StartingAngle Property (IHelixFeatureData)

Gets or sets the angle for the first turn of this helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Double

instance.StartingAngle = value

value = instance.StartingAngle
```

### C#

```csharp
System.double StartingAngle {get; set;}
```

### C++/CLI

```cpp
property System.double StartingAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle for the first turn

## VBA Syntax

See [HelixFeatureData::StartingAngle](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~StartingAngle.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
