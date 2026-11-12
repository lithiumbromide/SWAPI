---
title: "SpericalCenterDistance Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "SpericalCenterDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SpericalCenterDistance.html"
---

# SpericalCenterDistance Property (IMeasure)

Gets the distance between the two selected spherical faces.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SpericalCenterDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.SpericalCenterDistance
```

### C#

```csharp
System.double SpericalCenterDistance {get;}
```

### C++/CLI

```cpp
property System.double SpericalCenterDistance {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the two selected spherical faces or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::SpericalCenterDistance](ms-its:sldworksapivb6.chm::/Sldworks~Measure~SpericalCenterDistance.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
