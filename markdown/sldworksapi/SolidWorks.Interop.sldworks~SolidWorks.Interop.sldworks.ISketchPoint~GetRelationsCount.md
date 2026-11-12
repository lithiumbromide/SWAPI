---
title: "GetRelationsCount Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetRelationsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelationsCount.html"
---

# GetRelationsCount Method (ISketchPoint)

Gets the number of sketch relations for this sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelationsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Integer

value = instance.GetRelationsCount()
```

### C#

```csharp
System.int GetRelationsCount()
```

### C++/CLI

```cpp
System.int GetRelationsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch relations for this sketch point

## VBA Syntax

See [SketchPoint::GetRelationsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetRelationsCount.html).

## Remarks

Call this method before calling [ISketchPoint::IGetRelations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint~IGetRelations.html) to get the size of the array for that method.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)
[ISketchPoint::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
