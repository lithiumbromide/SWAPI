---
title: "Radius Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Radius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Radius.html"
---

# Radius Property (IMeasure)

Gets the radius of the selected arc or cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Radius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Radius
```

### C#

```csharp
System.double Radius {get;}
```

### C++/CLI

```cpp
property System.double Radius {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Radius

## VBA Syntax

See [Measure::Radius](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Radius.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Diameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Diameter.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
