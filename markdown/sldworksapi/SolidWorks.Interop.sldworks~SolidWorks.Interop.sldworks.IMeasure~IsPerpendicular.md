---
title: "IsPerpendicular Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "IsPerpendicular"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsPerpendicular.html"
---

# IsPerpendicular Property (IMeasure)

Gets whether the two selected entities are perpendicular.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsPerpendicular As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Boolean

value = instance.IsPerpendicular
```

### C#

```csharp
System.bool IsPerpendicular {get;}
```

### C++/CLI

```cpp
property System.bool IsPerpendicular {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the two selected entities are perpendicular, false if not

## VBA Syntax

See [Measure::IsPerpendicular](ms-its:sldworksapivb6.chm::/Sldworks~Measure~IsPerpendicular.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::IsConcentricSpheres Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsConcentricSpheres.html)
[IMeasure::IsIntersect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsIntersect.html)
[IMeasure::IsParallel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsParallel.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
