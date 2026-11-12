---
title: "DraftAngle Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftAngle.html"
---

# DraftAngle Property (ISimpleHoleFeatureData2)

Gets or sets the draft angle for this simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Double

instance.DraftAngle = value

value = instance.DraftAngle
```

### C#

```csharp
System.double DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Draft angle

## VBA Syntax

See [SimpleHoleFeatureData2::DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~DraftAngle.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftOutward.html)
[ISimpleHoleFeatureData2::DraftWhileExtruding Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
