---
title: "GetSketchPaths Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPaths"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPaths.html"
---

# GetSketchPaths Method (ISketch)

Gets the sketch paths in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPaths() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchPaths()
```

### C#

```csharp
System.object GetSketchPaths()
```

### C++/CLI

```cpp
System.Object^ GetSketchPaths();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch paths](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPath.html)

## VBA Syntax

See [Sketch::GetSketchPaths](ms-its:sldworksapivb6.chm::/Sldworks~Sketch~GetSketchPaths.html).

## Examples

[Create Sketch Path (VBA)](Create_Sketch_Path_Example_VB.htm)
[Create Sketch Path (VB.NET)](Create_Sketch_Path_Example_VBNET.htm)
[Create Sketch Path (C#)](Create_Sketch_Path_Example_CSharp.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPathCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPathCount.html)
[ISketch::IGetSketchPaths Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPaths.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
