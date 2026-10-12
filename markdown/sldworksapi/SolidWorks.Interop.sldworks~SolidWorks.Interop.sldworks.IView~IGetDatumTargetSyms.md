---
title: "IGetDatumTargetSyms Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDatumTargetSyms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTargetSyms.html"
---

# IGetDatumTargetSyms Method (IView)

Gets all of the datum target symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDatumTargetSyms( _
   ByVal NumDatumTargetSym As System.Integer _
) As DatumTargetSym
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDatumTargetSym As System.Integer
Dim value As DatumTargetSym

value = instance.IGetDatumTargetSyms(NumDatumTargetSym)
```

### C#

```csharp
DatumTargetSym IGetDatumTargetSyms(
   System.int NumDatumTargetSym
)
```

### C++/CLI

```cpp
DatumTargetSym^ IGetDatumTargetSyms(
   System.int NumDatumTargetSym
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDatumTargetSym`: Total number of datum target symbols on the drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum target symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of datum target symbols all at once instead of calling [IView::GetFirstDatumTargetSym](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumTargetSym.html) and then repeatedly calling [IDatumTargetSym::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetNext.html) to obtain the remaining datum target symbols on this drawing view.

Before calling this method, call [IView::GetDatumTargetSymCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDatumTargetSymCount.html) to get the value for numDatumTargetSym.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
