---
title: "GetFirstCenterMark2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstCenterMark2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark2.html"
---

# GetFirstCenterMark2 Method (IView)

Gets the first center mark in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCenterMark2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstCenterMark2()
```

### C#

```csharp
System.object GetFirstCenterMark2()
```

### C++/CLI

```cpp
System.Object^ GetFirstCenterMark2();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[center mark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html)

## VBA Syntax

See

[View::GetFirstCenterMark2](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstCenterMark2.html)

.

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)

[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)

[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

## Remarks

This method obsoletes IView::GetFirstCenterMark by supporting inactive sheets.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetCenterMarkCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.html)

[IView::GetCenterMarkInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html)

[IView::GetCenterMarks Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)

[ICenterMark::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
