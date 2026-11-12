---
title: "IGetCenterMarks Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetCenterMarks"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.html"
---

# IGetCenterMarks Method (IView)

Gets all of the center marks that are features in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCenterMarks( _
   ByVal Count As System.Integer _
) As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim value As CenterMark

value = instance.IGetCenterMarks(Count)
```

### C#

```csharp
CenterMark IGetCenterMarks(
   System.int Count
)
```

### C++/CLI

```cpp
CenterMark^ IGetCenterMarks(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of center marks that are features in the view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [centermarks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html) that are features in this view
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IView::GetCenterMarkCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterMarkCount2.html) to get the value for Count.

Center marks are now annotations. Previously, center marks were features. This method returns an empty array for center marks that are annotations; thus, this method is only valid for center marks that are features. See [ICenterMark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html) for details.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html)
[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)
[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.html)
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
