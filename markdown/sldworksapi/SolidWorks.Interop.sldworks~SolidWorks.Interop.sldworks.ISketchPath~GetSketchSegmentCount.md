---
title: "GetSketchSegmentCount Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetSketchSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegmentCount.html"
---

# GetSketchSegmentCount Method (ISketchPath)

Gets the number of sketch segments in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Integer

value = instance.GetSketchSegmentCount()
```

### C#

```csharp
System.int GetSketchSegmentCount()
```

### C++/CLI

```cpp
System.int GetSketchSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments

## VBA Syntax

See [SketchPath::GetSketchSegmentCount](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetSketchSegmentCount.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## Remarks

Call this method before calling [ISketch::IGetSketchSegments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath~IGetSketchSegments.html) to get the size of the array for that method.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[SketdhPath:;GetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegments.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
