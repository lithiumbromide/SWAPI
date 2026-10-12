---
title: "GetSketchPathCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPathCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPathCount.html"
---

# GetSketchPathCount Method (ISketch)

Gets the number of sketch paths in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPathCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
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

See [Sketch::GetSketchPathCount](ms-its:sldworksapivb6.chm::/Sldworks~Sketch~GetSketchPathCount.html).

## Remarks

Call this method before calling [ISketch::IGetSketchPaths](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchPaths.html) to get the sketch paths in this sketch.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPaths.html)
[ISketchPath Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
