---
title: "GetSketch Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetSketch.html"
---

# GetSketch Method (ISketchBlockInstance)

Gets the sketch in which this block instance is present.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
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

See [SketchBlockInstance::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetSketch.html).

## Examples

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::BlockToSketchTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~BlockToSketchTransform.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
