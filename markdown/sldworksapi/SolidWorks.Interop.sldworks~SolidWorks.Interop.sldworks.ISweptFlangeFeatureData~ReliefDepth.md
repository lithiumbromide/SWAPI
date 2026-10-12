---
title: "ReliefDepth Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "ReliefDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefDepth.html"
---

# ReliefDepth Property (ISweptFlangeFeatureData)

Gets or sets the bend relief depth for this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
Dim value As System.Double

instance.ReliefDepth = value

value = instance.ReliefDepth
```

### C#

```csharp
System.double ReliefDepth {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend relief depth

## VBA Syntax

See [SweptFlangeFeatureData::ReliefDepth](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~ReliefDepth.html).

## Remarks

This property is valid:

- If [ISweptFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseReliefRatio.html) is false,

- and -

- For regular swept flanges, but for cylindrical or conical swept flanges only during creation,

- and -

- When [ISweptFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.html) is [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes_e.swSheetMetalReliefObround.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
