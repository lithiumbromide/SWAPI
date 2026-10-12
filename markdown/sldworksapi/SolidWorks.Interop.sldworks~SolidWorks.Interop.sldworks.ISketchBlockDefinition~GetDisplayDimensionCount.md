---
title: "GetDisplayDimensionCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetDisplayDimensionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.html"
---

# GetDisplayDimensionCount Method (ISketchBlockDefinition)

Gets the number of display dimensions in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As System.Integer

value = instance.GetDisplayDimensionCount()
```

### C#

```csharp
System.int GetDisplayDimensionCount()
```

### C++/CLI

```cpp
System.int GetDisplayDimensionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of display dimensions

## VBA Syntax

See [SketchBlockDefinition::GetDisplayDimensionCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetDisplayDimensionCount.html).

## Examples

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
