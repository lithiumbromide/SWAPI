---
title: "GetDisplayDimensions Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html"
---

# GetDisplayDimensions Method (ISketchBlockDefinition)

Gets the display dimensions in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Object

value = instance.GetDisplayDimensions()
```

### C#

```csharp
System.object GetDisplayDimensions()
```

### C++/CLI

```cpp
System.Object^ GetDisplayDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [SketchBlockDefinition::GetDisplayDimensions](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetDisplayDimensions.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetDisplayDimensionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.html)
[ISketchBlockDefinition::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
