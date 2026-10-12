---
title: "TaperAngle Property (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "TaperAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~TaperAngle.html"
---

# TaperAngle Property (IHelixFeatureData)

Gets or sets the angle of the taper for this constant-pitch helix feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TaperAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim value As System.Double

instance.TaperAngle = value

value = instance.TaperAngle
```

### C#

```csharp
System.double TaperAngle {get; set;}
```

### C++/CLI

```cpp
property System.double TaperAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle of taper

## VBA Syntax

See [HelixFeatureData::TaperAngle](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~TaperAngle.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
