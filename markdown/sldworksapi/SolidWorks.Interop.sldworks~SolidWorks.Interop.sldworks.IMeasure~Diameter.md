---
title: "Diameter Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Diameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Diameter.html"
---

# Diameter Property (IMeasure)

Gets the diameter of the selected circle or cylinder.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Diameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Diameter
```

### C#

```csharp
System.double Diameter {get;}
```

### C++/CLI

```cpp
property System.double Diameter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Diameter of the selected circle or cylinder or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::Diameter](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Diameter.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Radius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Radius.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
