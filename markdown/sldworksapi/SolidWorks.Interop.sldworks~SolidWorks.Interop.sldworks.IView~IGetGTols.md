---
title: "IGetGTols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetGTols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.html"
---

# IGetGTols Method (IView)

Gets all of the geometric tolerances on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetGTols( _
   ByVal NumGTol As System.Integer _
) As Gtol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumGTol As System.Integer
Dim value As Gtol

value = instance.IGetGTols(NumGTol)
```

### C#

```csharp
Gtol IGetGTols(
   System.int NumGTol
)
```

### C++/CLI

```cpp
Gtol^ IGetGTols(
   System.int NumGTol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumGTol`: Total number of geometric tolerances on this drawing view.

### Return Value

- in-process, unmanaged C++: Pointer to an array of [geometric tolerances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of geometric tolerances all at once instead of calling [IView::GetFirstGTOL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstGTOL.html) and then repeatedly calling [IGtol::GetNextGTOL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetNextGTOL.html) to obtain the remaining geometric tolerances in the drawing view.

Before calling this method, call [IView::GetGTolCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetGtolCount.html) to get the value for numGTol.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
