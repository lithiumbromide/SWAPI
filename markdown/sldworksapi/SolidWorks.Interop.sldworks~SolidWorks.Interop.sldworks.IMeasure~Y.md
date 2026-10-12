---
title: "Y Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "Y"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Y.html"
---

# Y Property (IMeasure)

Gets the y coordinate of the selected point in model space.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Y As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Double

value = instance.Y
```

### C#

```csharp
System.double Y {get;}
```

### C++/CLI

```cpp
property System.double Y {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

y coordinate of the selected point in model space or -1 if this property is invalid for the selected entity

## VBA Syntax

See [Measure::Y](ms-its:sldworksapivb6.chm::/Sldworks~Measure~Y.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::X Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~X.html)
[IMeasure::Z Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Z.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
