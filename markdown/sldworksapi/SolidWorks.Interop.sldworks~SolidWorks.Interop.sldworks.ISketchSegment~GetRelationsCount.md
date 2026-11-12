---
title: "GetRelationsCount Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetRelationsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelationsCount.html"
---

# GetRelationsCount Method (ISketchSegment)

Gets the number of sketch relations for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelationsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

Number of sketch relations for this sketch segment

## VBA Syntax

See [SketchSegment::GetRelationsCount](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetRelationsCount.html).

## Remarks

Call this method before calling [ISketchSegment::IGetRelations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~IGetRelations.html) to get the size of the array for that method.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
