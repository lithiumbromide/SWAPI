---
title: "FlipView Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "FlipView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FlipView.html"
---

# FlipView Property (IView)

Gets or sets whether to flip a flat-pattern view of a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipView As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.FlipView = value

value = instance.FlipView
```

### C#

```csharp
System.bool FlipView {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipView {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the flat-pattern view, false to not

## VBA Syntax

See [View::FlipView](ms-its:sldworksapivb6.chm::/Sldworks~View~FlipView.html).

## Examples

[Create and Flip Flat-Pattern View of Sheet Metal Part (VBA)](Create_and_Flip_Flat-Pattern_View_of_Sheet_Metal_Part_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
