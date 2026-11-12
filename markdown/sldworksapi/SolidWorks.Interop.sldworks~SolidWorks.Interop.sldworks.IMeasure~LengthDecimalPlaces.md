---
title: "LengthDecimalPlaces Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "LengthDecimalPlaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~LengthDecimalPlaces.html"
---

# LengthDecimalPlaces Property (IMeasure)

Gets or sets the number of decimal places for length measurements.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthDecimalPlaces As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Integer

instance.LengthDecimalPlaces = value

value = instance.LengthDecimalPlaces
```

### C#

```csharp
System.int LengthDecimalPlaces {get; set;}
```

### C++/CLI

```cpp
property System.int LengthDecimalPlaces {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of decimal places for length measurements

## VBA Syntax

See [Measure::LengthDecimalPlaces](ms-its:sldworksapivb6.chm::/Sldworks~Measure~LengthDecimalPlaces.html).

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Length.html)
[IMeasure::TotalLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalLength.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
