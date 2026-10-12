---
title: "IGetDetail Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDetail"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html"
---

# IGetDetail Method (IView)

Gets the detail circle for this detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDetail() As DetailCircle
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DetailCircle

value = instance.IGetDetail()
```

### C#

```csharp
DetailCircle IGetDetail()
```

### C++/CLI

```cpp
DetailCircle^ IGetDetail();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Detail circle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle.html)

## VBA Syntax

See [View::IGetDetail](ms-its:sldworksapivb6.chm::/sldworks~View~IGetDetail.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[GetDetailCircleCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2.html)
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)
[IView::GetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.html)
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
