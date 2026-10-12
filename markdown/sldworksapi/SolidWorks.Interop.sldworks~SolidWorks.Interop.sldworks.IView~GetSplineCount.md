---
title: "GetSplineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSplineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSplineCount.html"
---

# GetSplineCount Method (IView)

Gets the number of splines in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineCount( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim PointCount As System.Integer
Dim value As System.Integer

value = instance.GetSplineCount(PointCount)
```

### C#

```csharp
System.int GetSplineCount(
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetSplineCount(
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`: Number of doubles (see [IView::GetSplines3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSplines3.html) or [IView::IGetSplines3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSplines3.html) Remarks)

### Return Value

Number of splines in the view

## VBA Syntax

See [View::GetSplineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetSplineCount.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
