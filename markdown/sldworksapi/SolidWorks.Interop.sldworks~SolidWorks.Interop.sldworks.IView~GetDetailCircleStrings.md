---
title: "GetDetailCircleStrings Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDetailCircleStrings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.html"
---

# GetDetailCircleStrings Method (IView)

Gets an array of strings; each string represents the text label for a detail circle in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetailCircleStrings() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDetailCircleStrings()
```

### C#

```csharp
System.object GetDetailCircleStrings()
```

### C++/CLI

```cpp
System.Object^ GetDetailCircleStrings();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings with one string for each detail circle in the view

## VBA Syntax

See [View::GetDetailCircleStrings](ms-its:sldworksapivb6.chm::/sldworks~View~GetDetailCircleStrings.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.html)
[IView::GetDetailCircleCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2.html)
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.html)
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.html)
