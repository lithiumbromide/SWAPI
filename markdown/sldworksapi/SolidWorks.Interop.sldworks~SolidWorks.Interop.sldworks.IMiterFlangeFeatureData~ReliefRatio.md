---
title: "ReliefRatio Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (IMiterFlangeFeatureData)

gets or sets the relief ratio for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Double

instance.ReliefRatio = value

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief ratio for rectangular or obround miter flanges

## VBA Syntax

See [MiterFlangeFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~ReliefRatio.html).

## Remarks

SOLIDWORKS uses this property only if [IMiterMiterFlangeFeatureData::UseReliefRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.html) is True. If IMiterMiterFlangeFeatureData::UseReliefRatio is false, then SOLIDWORKS uses [IMiterFlangeFeatureData::ReliefDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefDepth.html) with [IMiterFlangeFeatureData::ReliefWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefWidth.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::ReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefType.html)
[IMiterFlangeFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRelief.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
