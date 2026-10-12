---
title: "GetSketch Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSketch.html"
---

# GetSketch Method (ISketchBlockDefinition)

Gets the underlying sketch of this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
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

Underlying [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SketchBlockDefinition::GetSketch](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetSketch.html).

## Remarks

The returned sketch defines this block. The sketch does not appear in the FeatureManager tree.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
