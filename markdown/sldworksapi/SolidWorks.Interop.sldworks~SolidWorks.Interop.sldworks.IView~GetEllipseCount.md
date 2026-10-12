---
title: "GetEllipseCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetEllipseCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetEllipseCount.html"
---

# GetEllipseCount Method (IView)

Gets the number of ellipses in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEllipseCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetEllipseCount()
```

### C#

```csharp
System.int GetEllipseCount()
```

### C++/CLI

```cpp
System.int GetEllipseCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of ellipses in the view

## VBA Syntax

See [View::GetEllipseCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetEllipseCount.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetEllipses5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetEllipses5.html) to get the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
