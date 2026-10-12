---
title: "IGetDatumOrigins Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDatumOrigins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.html"
---

# IGetDatumOrigins Method (IView)

Gets all of the datum origins on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDatumOrigins( _
   ByVal NumDatumOrigin As System.Integer _
) As DatumOrigin
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDatumOrigin As System.Integer
Dim value As DatumOrigin

value = instance.IGetDatumOrigins(NumDatumOrigin)
```

### C#

```csharp
DatumOrigin IGetDatumOrigins(
   System.int NumDatumOrigin
)
```

### C++/CLI

```cpp
DatumOrigin^ IGetDatumOrigins(
   System.int NumDatumOrigin
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDatumOrigin`: Total number of datum origins on the drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum origins](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of datum origins all at once instead of calling [IView::GetFirstDatumOrigin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumOrigin.html) and then repeatedly calling [IDatumOrigin::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin~GetNext.html) to obtain the remaining datum origins on this drawing view.

Before calling this method, call [IView::GetDatumOriginCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDatumOriginCount.html) to get the value for numDatumOrigin.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumOriginCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.html)
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
