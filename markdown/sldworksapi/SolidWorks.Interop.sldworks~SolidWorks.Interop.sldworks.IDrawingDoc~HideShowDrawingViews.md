---
title: "HideShowDrawingViews Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "HideShowDrawingViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDrawingViews.html"
---

# HideShowDrawingViews Method (IDrawingDoc)

Sets whether to hide or show hidden drawing views.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideShowDrawingViews()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.HideShowDrawingViews()
```

### C#

```csharp
void HideShowDrawingViews()
```

### C++/CLI

```cpp
void HideShowDrawingViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::HideShowDrawingViews](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~HideShowDrawingViews.html).

## Examples

[Display Hidden Lines in Drawing (VBA)](Display_Hidden_Lines_in_Drawing_Example_VB.htm)
[Display Hidden Lines in Drawing (VB.NET)](Display_Hidden_Lines_in_Drawing_Example_VBNET.htm)
[Display Hidden Lines in Drawing (C#)](Display_Hidden_Lines_in_Drawing_Example_CSharp.htm)

## Remarks

If this setting is enabled, then SOLIDWORKS shows drawing views that were hidden using [IDrawingDoc::SuppressView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~SuppressView.html) with an **X**.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html)
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.html)
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.html)
[IDrawingDoc::ViewDisplayHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayHidden.html)
[IDrawingDoc::ViewDisplayHiddengreyed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayHiddengreyed.html)
[IDrawingDoc::ViewDisplayShaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayShaded.html)
[IDrawingDoc::ViewDisplayWireframe Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewDisplayWireframe.html)
[IDrawingDoc::ViewFullPage Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewFullPage.html)
[IDrawingDoc::ViewHlrQuality Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ViewHlrQuality.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::AutomaticViewUpdate Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutomaticViewUpdate.html)
[IDrawingDoc::HiddenViewsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HiddenViewsVisible.html)
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
