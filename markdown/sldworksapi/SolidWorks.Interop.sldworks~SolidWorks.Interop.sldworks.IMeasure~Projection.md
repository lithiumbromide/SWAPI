---
title: "Projection Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Projection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection.html"
---

# Projection Property (IMeasure)

Gets the projected distance between the two selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Projection As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Projection
```

### C#

```csharp
System.double Projection {get;}
```

### C++/CLI

```cpp
property System.double Projection {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Projected distance between the two selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::Projection](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Projection.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::ProjectionOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption.html)
[IMeasure::SetProjectionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
