---
title: "NormalDistance Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "NormalDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~NormalDistance.html"
---

# NormalDistance Property (IMeasure)

Gets the normal distance (normal to the selected plane) between the selected entity and plane.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NormalDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.NormalDistance
```

### C#

```csharp
System.double NormalDistance {get;}
```

### C++/CLI

```cpp
property System.double NormalDistance {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Normal distance or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::NormalDistance](ms-its:sldworksapivb6.chm::/Sldworks~Measure~NormalDistance.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Normal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Normal.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
