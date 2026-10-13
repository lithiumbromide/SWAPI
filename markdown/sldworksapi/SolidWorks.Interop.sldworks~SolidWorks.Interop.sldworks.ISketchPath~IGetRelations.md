---
title: "IGetRelations Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "IGetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetRelations.html"
---

# IGetRelations Method (ISketchPath)

Gets the sketch relations for this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRelations( _
   ByVal Count As System.Integer _
) As SketchRelation
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
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

Before calling this method, call [ISketchPath::GetRelationsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~GetRelationsCount.html) to get the value of Count.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetRelations.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
