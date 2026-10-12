---
title: "GetFirstDatumOrigin Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstDatumOrigin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin.html"
---

# GetFirstDatumOrigin Method (IView)

Gets the first datum origin in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDatumOrigin() As DatumOrigin
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DatumOrigin

value = instance.GetFirstDatumOrigin()
```

### C#

```csharp
DatumOrigin GetFirstDatumOrigin()
```

### C++/CLI

```cpp
DatumOrigin^ GetFirstDatumOrigin();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [datum origin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin.html)

## VBA Syntax

See [View::GetFirstDatumOrigin](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstDatumOrigin.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDatumOrigin::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext.html)
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.html)
[IView::IGetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
