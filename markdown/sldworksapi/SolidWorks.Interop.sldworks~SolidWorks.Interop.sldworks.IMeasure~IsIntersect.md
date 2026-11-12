---
title: "IsIntersect Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "IsIntersect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsIntersect.html"
---

# IsIntersect Property (IMeasure)

Gets whether the two selected entities intersect.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsIntersect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Boolean

value = instance.IsIntersect
```

### C#

```csharp
System.bool IsIntersect {get;}
```

### C++/CLI

```cpp
property System.bool IsIntersect {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the two selected entities intersect, false if not

## VBA Syntax

See [Measure::IsIntersect](ms-its:sldworksapivb6.chm::/Sldworks~Measure~IsIntersect.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::IsConcentricSpheres Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsConcentricSpheres.html)
[IMeasure::IsParallel Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsParallel.html)
[IMeasure::IsPerpendicular Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsPerpendicular.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
