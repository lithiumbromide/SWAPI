---
title: "Length Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Length.html"
---

# Length Property (IMeasure)

Gets the length of the selected entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Length
```

### C#

```csharp
System.double Length {get;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of the selected entity or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::Length](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Length.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::LengthDecimalPlaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~LengthDecimalPlaces.html)
[IMeasure::TotalLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~TotalLength.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
