---
title: "AngleDecimalPlaces Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "AngleDecimalPlaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~AngleDecimalPlaces.html"
---

# AngleDecimalPlaces Property (IMeasure)

Gets or sets the number of decimal places for angle measurements.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngleDecimalPlaces As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Integer

instance.AngleDecimalPlaces = value

value = instance.AngleDecimalPlaces
```

### C#

```csharp
System.int AngleDecimalPlaces {get; set;}
```

### C++/CLI

```cpp
property System.int AngleDecimalPlaces {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of decimal places for angle measurements

## VBA Syntax

See [Measure::AngleDecimalPlaces](ms-its:sldworksapivb6.chm::/Sldworks~Measure~AngleDecimalPlaces.html).

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Angle.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
