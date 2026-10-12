---
title: "TotalArea Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "TotalArea"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalArea.html"
---

# TotalArea Property (IMeasure)

Gets the total area of the two selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TotalArea As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.TotalArea
```

### C#

```csharp
System.double TotalArea {get;}
```

### C++/CLI

```cpp
property System.double TotalArea {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total area of the two selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::TotalArea](ms-its:sldworksapivb6.chm::/Sldworks~Measure~TotalArea.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Area Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Area.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
