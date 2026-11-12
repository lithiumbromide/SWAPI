---
title: "ReliefType Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "ReliefType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefType.html"
---

# ReliefType Property (IMiterFlangeFeatureData)

Gets or sets the relief type for this miter flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Integer

instance.ReliefType = value

value = instance.ReliefType
```

### C#

```csharp
System.int ReliefType {get; set;}
```

### C++/CLI

```cpp
property System.int ReliefType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief type as defined in [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

## VBA Syntax

See [MiterFlangeFeatureData::ReliefType](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~ReliefType.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefDepth.html)
[IMiterFlangeFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefRatio.html)
[IMiterFlangeFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~ReliefWidth.html)
[IMiterFlangeFeatureData::UseReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseReliefRatio.html)
[IMiterFlangeFeatureData::UseDefaultBendRelief Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRelief.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
