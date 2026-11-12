---
title: "GetTemporaryAxesCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetTemporaryAxesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxesCount.html"
---

# GetTemporaryAxesCount Method (IView)

Gets the number of temporary axes in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemporaryAxesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetTemporaryAxesCount()
```

### C#

```csharp
System.int GetTemporaryAxesCount()
```

### C++/CLI

```cpp
System.int GetTemporaryAxesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of temporary axes in this view

## VBA Syntax

See [View::GetTemporaryAxesCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetTemporaryAxesCount.html).

## Examples

[Get Temporary Axes in Each Drawing View (VBA)](Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetTemporaryAxes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetTemporaryAxes.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
