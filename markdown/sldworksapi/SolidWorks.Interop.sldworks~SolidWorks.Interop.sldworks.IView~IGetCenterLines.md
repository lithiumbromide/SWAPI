---
title: "IGetCenterLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetCenterLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterLines.html"
---

# IGetCenterLines Method (IView)

Gets all of the centerlines on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCenterLines( _
   ByVal NumCenterLine As System.Integer _
) As Centerline
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumCenterLine As System.Integer
Dim value As Centerline

value = instance.IGetCenterLines(NumCenterLine)
```

### C#

```csharp
Centerline IGetCenterLines(
   System.int NumCenterLine
)
```

### C++/CLI

```cpp
Centerline^ IGetCenterLines(
   System.int NumCenterLine
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumCenterLine`: Total number of centerlines on this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [centerlines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of centerlines all at once instead of calling [IView::GetFirstCenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstCenterLine.html) and then repeatedly calling [ICenterLine::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine~GetNext.html) to obtain the remaining centerlines on the drawing view.

Before calling this method, call [IView::GetCenterLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterLineCount.html) to get the value for numCenterLine.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
