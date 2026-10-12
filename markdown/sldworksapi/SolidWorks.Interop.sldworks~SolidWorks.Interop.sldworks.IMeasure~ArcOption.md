---
title: "ArcOption Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "ArcOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcOption.html"
---

# ArcOption Property (IMeasure)

Gets or sets how to measure an arc or circle.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArcOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Integer

instance.ArcOption = value

value = instance.ArcOption
```

### C#

```csharp
System.int ArcOption {get; set;}
```

### C++/CLI

```cpp
property System.int ArcOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

How to measure an arc or circle as defined by [swMeasureArcCircleOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMeasureArcCircleOption_e.html)

## VBA Syntax

See [Measure::ArcOption](ms-its:sldworksapivb6.chm::/Sldworks~Measure~ArcOption.html).

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::ArcLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcLength.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
