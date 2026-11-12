---
title: "IGetDisplayDimensions Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "IGetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetDisplayDimensions.html"
---

# IGetDisplayDimensions Method (ISketchBlockDefinition)

Gets the display dimensions in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayDimensions( _
   ByVal Count As System.Integer _
) As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim Count As System.Integer
Dim value As DisplayDimension

value = instance.IGetDisplayDimensions(Count)
```

### C#

```csharp
DisplayDimension IGetDisplayDimensions(
   System.int Count
)
```

### C++/CLI

```cpp
DisplayDimension^ IGetDisplayDimensions(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of display dimensions

### Return Value

- in-process, unmanaged C++: Pointer to an array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISketchBlockDefinition::GetDisplayDimensionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensionCount.html) before calling this method to get the value of Count.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
