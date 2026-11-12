---
title: "Perimeter Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Perimeter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Perimeter.html"
---

# Perimeter Property (IMeasure)

Gets the perimeter of the selected entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Perimeter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Perimeter
```

### C#

```csharp
System.double Perimeter {get;}
```

### C++/CLI

```cpp
property System.double Perimeter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Perimeter of the selected entity or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::Perimeter](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Perimeter.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
