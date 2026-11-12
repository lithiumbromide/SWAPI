---
title: "DeltaY Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "DeltaY"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~DeltaY.html"
---

# DeltaY Property (IMeasure)

Gets the Delta Y distance between the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DeltaY As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.DeltaY
```

### C#

```csharp
System.double DeltaY {get;}
```

### C++/CLI

```cpp
property System.double DeltaY {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Delta Y distance between the selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::DeltaY](ms-its:sldworksapivb6.chm::/Sldworks~Measure~DeltaY.html).

## Examples

See the [IMeasure](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html) examples.

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
