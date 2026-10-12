---
title: "HiddenViewsVisible Property (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "HiddenViewsVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HiddenViewsVisible.html"
---

# HiddenViewsVisible Property (IDrawingDoc)

Shows or hides all of the hidden drawing views.

## Syntax

### Visual Basic (Declaration)

```vb
Property HiddenViewsVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

instance.HiddenViewsVisible = value

value = instance.HiddenViewsVisible
```

### C#

```csharp
System.bool HiddenViewsVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool HiddenViewsVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if views are visible, false if they are hidden

## VBA Syntax

See [DrawingDoc::HiddenViewsVisible](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~HiddenViewsVisible.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.html)
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.html)
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
