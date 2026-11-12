---
title: "Angle Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Angle.html"
---

# Angle Property (IMeasure)

Gets the angle between the two selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Angle
```

### C#

```csharp
System.double Angle {get;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians between the two selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::Angle](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Angle.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::AngleDecimalPlaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~AngleDecimalPlaces.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
