---
title: "ArcLength Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "ArcLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcLength.html"
---

# ArcLength Property (IMeasure)

Gets the length of the selected arc.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ArcLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.ArcLength
```

### C#

```csharp
System.double ArcLength {get;}
```

### C++/CLI

```cpp
property System.double ArcLength {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of arc or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::ArcLength](ms-its:sldworksapivb6.chm::/Sldworks~Measure~ArcLength.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::ArcOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ArcOption.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
