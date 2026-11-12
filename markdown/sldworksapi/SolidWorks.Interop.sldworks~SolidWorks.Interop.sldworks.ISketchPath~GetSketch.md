---
title: "GetSketch Method (ISketchPath)"
project: "SOLIDWORKS API Help"
interface: "ISketchPath"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath~GetSketch.html"
---

# GetSketch Method (ISketchPath)

Gets the sketch where this sketch path exists.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPath
Dim value As Sketch

value = instance.GetSketch()
```

### C#

```csharp
Sketch GetSketch()
```

### C++/CLI

```cpp
Sketch^ GetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchPath::GetSketch](ms-its:sldworksapivb6.chm::/Sldworks~SketchPath~GetSketch.html).

## See Also

[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)
[ISketchPath Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html)

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
