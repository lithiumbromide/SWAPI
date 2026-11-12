---
title: "GetDetail Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDetail"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetail.html"
---

# GetDetail Method (IView)

Gets the detail circle for this detail view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetail() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDetail()
```

### C#

```csharp
System.object GetDetail()
```

### C++/CLI

```cpp
System.Object^ GetDetail();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Detail circle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDetailCircle.html)

## VBA Syntax

See [View::GetDetail](ms-its:sldworksapivb6.chm::/sldworks~View~GetDetail.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDetailCircleCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleCount2.html)
[IView::GetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleInfo2.html)
[IView::GetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircles.html)
[IView::GetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDetailCircleStrings.html)
[IView::IGetDetail Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetail.html)
[IView::IGetDetailCircleInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleInfo2.html)
[IView::IGetDetailCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircles.html)
[IView::IGetDetailCircleStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDetailCircleStrings.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
