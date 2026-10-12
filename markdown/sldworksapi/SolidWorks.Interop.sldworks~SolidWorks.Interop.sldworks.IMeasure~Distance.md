---
title: "Distance Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Distance.html"
---

# Distance Property (IMeasure)

Gets the distance between the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Distance
```

### C#

```csharp
System.double Distance {get;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::Distance](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Distance.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
