---
title: "X Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "X"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~X.html"
---

# X Property (IMeasure)

Gets the x coordinate of the selected point in model space.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property X As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.X
```

### C#

```csharp
System.double X {get;}
```

### C++/CLI

```cpp
property System.double X {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate of the selected point in model space or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::X](ms-its:sldworksapivb6.chm::/Sldworks~Measure~X.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure:Y Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Y.html)
[IMeasure::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Z.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
