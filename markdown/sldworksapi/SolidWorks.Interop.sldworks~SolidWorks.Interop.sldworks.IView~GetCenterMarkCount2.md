---
title: "GetCenterMarkCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCenterMarkCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.html"
---

# GetCenterMarkCount2 Method (IView)

Gets the number of center marks that are features in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterMarkCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetCenterMarkCount2(Size)
```

### C#

```csharp
System.int GetCenterMarkCount2(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetCenterMarkCount2(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Not used

### Return Value

Number of center marks in the view

## VBA Syntax

See [View::GetCenterMarkCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetCenterMarkCount2.html).

## Remarks

Center marks are now annotations. Previously, center marks were features. This method is only valid for center marks that are features.

One difference between this method and the now obsolete [IView::GetCenterMarkCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterMarkCount.html) is that this method also works if this view represents the drawing sheet. The original method always returns 0 if this view is the drawing sheet.

Call this method before calling [IView::IGetCenterMarks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetCenterMarks.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html)
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.html)
[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.html)
[IView::GetFirstCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.html)
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
