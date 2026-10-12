---
title: "DeltaZ Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "DeltaZ"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~DeltaZ.html"
---

# DeltaZ Property (IMeasure)

Gets the Delta Z distance between the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DeltaZ As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.DeltaZ
```

### C#

```csharp
System.double DeltaZ {get;}
```

### C++/CLI

```cpp
property System.double DeltaZ {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Delta Z distance between the selected entities or -1 if this property is invalid for the selected entities

## VBA Syntax

See [Measure::DeltaZ](ms-its:sldworksapivb6.chm::/Sldworks~Measure~DeltaZ.html).

## Examples

See the [IMeasure](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html) examples.

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
