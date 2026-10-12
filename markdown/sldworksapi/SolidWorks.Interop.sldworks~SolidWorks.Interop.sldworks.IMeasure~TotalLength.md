---
title: "TotalLength Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "TotalLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalLength.html"
---

# TotalLength Property (IMeasure)

Gets the total length of the two selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TotalLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.TotalLength
```

### C#

```csharp
System.double TotalLength {get;}
```

### C++/CLI

```cpp
property System.double TotalLength {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total length of the two selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::TotalLength](ms-its:sldworksapivb6.chm::/Sldworks~Measure~TotalLength.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Length.html)
[IMeasure::LengthDecimalPlaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~LengthDecimalPlaces.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
