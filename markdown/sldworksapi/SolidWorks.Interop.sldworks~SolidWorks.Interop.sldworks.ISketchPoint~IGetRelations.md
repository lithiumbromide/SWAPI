---
title: "IGetRelations Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "IGetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetRelations.html"
---

# IGetRelations Method (ISketchPoint)

Gets the sketch relations for this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRelations( _
   ByVal Count As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim Count As System.Integer
Dim value As SketchRelation

value = instance.IGetRelations(Count)
```

### C#

```csharp
SketchRelation IGetRelations(
   System.int Count
)
```

### C++/CLI

```cpp
SketchRelation^ IGetRelations(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch relations

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchPoint::GetRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~GetRelationsCount.html) to get the value for Count.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
