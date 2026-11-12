---
title: "IGetTemporaryAxes Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetTemporaryAxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTemporaryAxes.html"
---

# IGetTemporaryAxes Method (IView)

Gets the information of the temporary axes displayed in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTemporaryAxes( _
   ByVal TempAxesCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim TempAxesCount As System.Integer
Dim value As System.Double

value = instance.IGetTemporaryAxes(TempAxesCount)
```

### C#

```csharp
System.double IGetTemporaryAxes(
   System.int TempAxesCount
)
```

### C++/CLI

```cpp
System.double IGetTemporaryAxes(
   System.int TempAxesCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TempAxesCount`: Number of temporary axes

  \

## VBA Syntax

See [View::IGetTemporaryAxes](ms-its:sldworksapivb6.chm::/sldworks~View~IGetTemporaryAxes.html).

## Remarks

Call [IView::GetTemporaryAxesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetTemporaryAxesCount.html) before calling this method to get the value for TempAxesCount.

This array contains the start and end points, in that order, of temporary axes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetTemporaryAxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTemporaryAxes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
