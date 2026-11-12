---
title: "GetBaseView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBaseView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBaseView.html"
---

# GetBaseView Method (IView)

Gets the base (parent) view used to create this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBaseView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetBaseView()
```

### C#

```csharp
System.object GetBaseView()
```

### C++/CLI

```cpp
System.Object^ GetBaseView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Base [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [View::GetBaseView](ms-its:sldworksapivb6.chm::/sldworks~View~GetBaseView.html).

## Examples

[Get Base Views (VBA)](Get_Base_Views_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetBaseView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBaseView.html)
[IView::GetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNextView.html)
[IView::IGetNextView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNextView.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
