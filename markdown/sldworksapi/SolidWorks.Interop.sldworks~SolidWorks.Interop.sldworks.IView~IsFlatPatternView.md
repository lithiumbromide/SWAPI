---
title: "IsFlatPatternView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsFlatPatternView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.html"
---

# IsFlatPatternView Method (IView)

Gets whether a drawing view is a flat-pattern drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsFlatPatternView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsFlatPatternView()
```

### C#

```csharp
System.bool IsFlatPatternView()
```

### C++/CLI

```cpp
System.bool IsFlatPatternView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this drawing view is a flat-pattern drawing view, false if not

## VBA Syntax

See [View::IsFlatPatternView](ms-its:sldworksapivb6.chm::/sldworks~View~IsFlatPatternView.html).

## Examples

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDrawingDoc::CreateFlatPatternViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
