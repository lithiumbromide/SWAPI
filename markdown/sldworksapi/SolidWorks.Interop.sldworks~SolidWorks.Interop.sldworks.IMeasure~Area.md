---
title: "Area Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Area"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Area.html"
---

# Area Property (IMeasure)

Gets the area of the selected entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Area As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Area
```

### C#

```csharp
System.double Area {get;}
```

### C++/CLI

```cpp
property System.double Area {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Area or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::Area](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Area.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::TotalArea Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalArea.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
