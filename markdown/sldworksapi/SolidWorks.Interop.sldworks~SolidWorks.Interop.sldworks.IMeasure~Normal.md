---
title: "Normal Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Normal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Normal.html"
---

# Normal Property (IMeasure)

Gets the normal distance (normal to the selected plane) between the selected face and plane.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Normal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Normal
```

### C#

```csharp
System.double Normal {get;}
```

### C++/CLI

```cpp
property System.double Normal {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Normal distance between the selected face and plane or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::Normal](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Normal.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::NormalDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~NormalDistance.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
