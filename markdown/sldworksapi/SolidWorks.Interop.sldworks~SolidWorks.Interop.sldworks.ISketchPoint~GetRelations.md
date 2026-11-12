---
title: "GetRelations Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelations.html"
---

# GetRelations Method (ISketchPoint)

Gets the sketch relations for this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Object

value = instance.GetRelations()
```

### C#

```csharp
System.object GetRelations()
```

### C++/CLI

```cpp
System.Object^ GetRelations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

## VBA Syntax

See [SketchPoint::GetRelations](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetRelations.html).

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelationsCount.html)
[ISketchPoint::IGetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
