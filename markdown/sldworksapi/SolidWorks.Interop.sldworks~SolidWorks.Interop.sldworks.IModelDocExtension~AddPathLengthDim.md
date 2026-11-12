---
title: "AddPathLengthDim Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddPathLengthDim"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddPathLengthDim.html"
---

# AddPathLengthDim Method (IModelDocExtension)

Inserts a path length dimension at the specified coordinates for a selected path.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPathLengthDim( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object

value = instance.AddPathLengthDim(X, Y, Z)
```

### C#

```csharp
System.object AddPathLengthDim(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.Object^ AddPathLengthDim(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of display dimension
- `Y`: Y coordinate of display dimension
- `Z`: Z coordinate of display dimension

### Return Value

[IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [ModelDocExtension::AddPathLengthDim](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~AddPathLengthDim.html).

## Examples

[Create Path Length Dimension (VBA)](Create_Path_Length_Dimension_Example_VB.htm)
[Create Path Length Dimension (VB.NET)](Create_Path_Length_Dimension_Example_VBNET.htm)
[Create Path Length Dimension (C#)](Create_Path_Length_Dimension_Example_CSharp.htm)

## Remarks

Before calling this method to create a path length dimension:

| If a path... | Then... |
| --- | --- |
| Exists | Call IModelDocExtension::SelectByID2 to select one sketch segment on the existing path. |
| Does not exist | Call IModelDocExtension::SelectByID2 to select two or more sketch segments that are end-to-end coincident and form a single chain. Call ISketchManager::MakeSketchChain to create a path with the selected sketch segments. Call IModelDocExtension::SelectByID2 to select one sketch segment on the path. |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
