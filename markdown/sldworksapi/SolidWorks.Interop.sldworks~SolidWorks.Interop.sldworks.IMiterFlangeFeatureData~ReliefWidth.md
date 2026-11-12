---
title: "ReliefWidth Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "ReliefWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefWidth.html"
---

# ReliefWidth Property (IMiterFlangeFeatureData)

Gets or sets the relief width for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Double

instance.ReliefWidth = value

value = instance.ReliefWidth
```

### C#

```csharp
System.double ReliefWidth {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief width for this miter flange

## VBA Syntax

See [MiterFlangeFeatureData::ReliefWidth](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~ReliefWidth.html).

## Remarks

SOLIDWORKS uses this property with [IMiterFlangeFeatureData::ReliefDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefDepth.html) only if [IMiterMiterFlangeFeatureData::UseReliefRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.html) is false. If [IMiterMiterFlangeFeatureData::UseReliefRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.html) is True, then SOLIDWORKS uses [IMiterMiterFlangeFeatureData::ReliefRatio](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData~ReliefRatio.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::ReliefType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefType.html)
[IMiterFlangeFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRelief.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
