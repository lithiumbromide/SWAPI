---
title: "ChordLength Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "ChordLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ChordLength.html"
---

# ChordLength Property (IMeasure)

Gets the chord length of the selected arc.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ChordLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.ChordLength
```

### C#

```csharp
System.double ChordLength {get;}
```

### C++/CLI

```cpp
property System.double ChordLength {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Chord length or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::ChordLength](ms-its:sldworksapivb6.chm::/Sldworks~Measure~ChordLength.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
