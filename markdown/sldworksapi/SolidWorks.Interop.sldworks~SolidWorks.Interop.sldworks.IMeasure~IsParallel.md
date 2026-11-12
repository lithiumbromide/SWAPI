---
title: "IsParallel Property (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "IsParallel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsParallel.html"
---

# IsParallel Property (IMeasure)

Gets whether the two selected entities are parallel.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsParallel As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim value As System.Boolean

value = instance.IsParallel
```

### C#

```csharp
System.bool IsParallel {get;}
```

### C++/CLI

```cpp
property System.bool IsParallel {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the two selected entities are parallel, false if not

## VBA Syntax

See [Measure::IsParallel](ms-its:sldworksapivb6.chm::/Sldworks~Measure~IsParallel.html).

## Examples

[Measure Selected Entities (C#)](Measure_Selected_Entities_Example_CSharp.htm)
[Measure Selected Entities (VB.NET)](Measure_Selected_Entities_Example_VBNET.htm)
[Measure Selected Entities (VBA)](Measure_Selected_Entities_Example_VB.htm)

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::IsConcentricSpheres Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsConcentricSpheres.html)
[IMeasure::IsIntersect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsIntersect.html)
[IMeasure::IsPerpendicular Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~IsPerpendicular.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
