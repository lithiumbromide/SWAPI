---
title: "HiddenEdges Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "HiddenEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HiddenEdges.html"
---

# HiddenEdges Property (IView)

Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible.

## Syntax

### Visual Basic (Declaration)

```vb
Property HiddenEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

instance.HiddenEdges = value

value = instance.HiddenEdges
```

### C#

```csharp
System.object HiddenEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ HiddenEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of hidden [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [View::HiddenEdges](ms-its:sldworksapivb6.chm::/sldworks~View~HiddenEdges.html).

## Examples

[Hide and Show All Edges in Drawing View (C#)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_CSharp.htm)
[Hide and Show All Edges in Drawing View (VB.NET)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_VBNET.htm)
[Hide and Show All Edges in Drawing View (VBA)](Hide_and_Show_All_Edges_in_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDrawingDoc::HideEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideEdge.html)
[IDrawingDoc::ShowEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ShowEdge.html)

## Availability

SOLIDWORKS 2008 SP5, Revision Number 16.5
