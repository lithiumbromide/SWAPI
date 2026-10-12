---
title: "GetSketchSegments Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetSketchSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegments.html"
---

# GetSketchSegments Method (ISketchPath)

Gets the sketch segments in this sketch path.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As System.Object

value = instance.GetSketchSegments()
```

### C#

```csharp
System.object GetSketchSegments()
```

### C++/CLI

```cpp
System.Object^ GetSketchSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [SketchPath::GetSketchSegments](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetSketchSegments.html).

## Examples

See the [ISketchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html) examples.

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)
[ISketchPath::GetSketchSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketchSegmentCount.html)
[ISketchPath::IGetSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~IGetSketchSegments.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
