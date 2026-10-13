---
title: "GetOutline Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetOutline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOutline.html"
---

# GetOutline Method (IView)

Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOutline() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetOutline()
```

### C#

```csharp
System.object GetOutline()
```

### C++/CLI

```cpp
System.Object^ GetOutline();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::GetOutline](ms-its:sldworksapivb6.chm::/sldworks~View~GetOutline.html).

## Examples

[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

## Remarks

The return value is an array of 4 doubles with the following format:

- 0, X min
- 1, Y min
- 2, X max
- 3, Y max

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetOutline.html)
