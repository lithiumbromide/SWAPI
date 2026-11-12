---
title: "CenterDistance Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "CenterDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~CenterDistance.html"
---

# CenterDistance Property (IMeasure)

Gets the distance between the selected cylinder axes, circle centers, or both.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CenterDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.CenterDistance
```

### C#

```csharp
System.double CenterDistance {get;}
```

### C++/CLI

```cpp
property System.double CenterDistance {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between cylinder axes, circle centers, or both or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::CenterDistance](ms-its:sldworksapivb6.chm::/Sldworks~Measure~CenterDistance.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
