---
title: "GetSketchPathCount Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetSketchPathCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPathCount.html"
---

# GetSketchPathCount Method (ISketchSegment)

Gets the number of sketch paths for this sketch segment

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPathCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Integer

value = instance.GetSketchPathCount()
```

### C#

```csharp
System.int GetSketchPathCount()
```

### C++/CLI

```cpp
System.int GetSketchPathCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch paths

## VBA Syntax

See [SketchSegment::GetSketchPathCount](ms-its:sldworksapivb6.chm::/Sldworks~SketchSegment~GetSketchPathCount.html).

## Remarks

Call this method before calling [ISketchSegment::IGetSketchPaths](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment~IGetSketchPaths.html) to get the size of the array for that method.

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetSketchPaths.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
