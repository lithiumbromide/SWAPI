---
title: "IGetRelations Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetRelations.html"
---

# IGetRelations Method (ISketchSegment)

Gets the sketch relations for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRelations( _
   ByVal Count As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

- `Count`: Number of sketch relations for this sketch segment

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html) for this sketch segment

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISketchSegment::GetRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~GetRelationsCount.html) to get the value for Count.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
