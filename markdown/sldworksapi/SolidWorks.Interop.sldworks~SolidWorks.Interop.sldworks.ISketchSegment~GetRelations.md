---
title: "GetRelations Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetRelations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelations.html"
---

# GetRelations Method (ISketchSegment)

Gets the sketch relations for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRelations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
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

Array of [sketch relations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRelation.html) for this sketch segment

## VBA Syntax

See [SketchSegment::GetRelations](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetRelations.html).

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetRelationsCount.html)
[ISketchSegment::IGetRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetRelations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
