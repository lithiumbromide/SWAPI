---
title: "IGetWeldBeads Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetWeldBeads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads.html"
---

# IGetWeldBeads Method (IView)

Gets all of the weld beads on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWeldBeads( _
   ByVal NumWeldBead As System.Integer _
) As WeldBead
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumWeldBead As System.Integer
Dim value As WeldBead

value = instance.IGetWeldBeads(NumWeldBead)
```

### C#

```csharp
WeldBead IGetWeldBeads(
   System.int NumWeldBead
)
```

### C++/CLI

```cpp
WeldBead^ IGetWeldBeads(
   System.int NumWeldBead
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumWeldBead`: Total number of weld beads on this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [weld beads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of weld beads all at once instead of calling [IView::GetFirstWeldBead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstWeldBead.html) and then repeatedly calling [IWeldBead::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead~GetNext.html) to obtain the weld beads in the drawing view.

Before calling this method, call [IView::GetWeldBeadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetWeldBeadCount.html) to get the value for numWeldBead.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
