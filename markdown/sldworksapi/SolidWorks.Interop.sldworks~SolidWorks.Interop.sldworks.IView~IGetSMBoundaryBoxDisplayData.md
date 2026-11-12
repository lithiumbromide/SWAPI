---
title: "IGetSMBoundaryBoxDisplayData Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetSMBoundaryBoxDisplayData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSMBoundaryBoxDisplayData.html"
---

# IGetSMBoundaryBoxDisplayData Method (IView)

Gets the boundary-box sketch display data of a flat-pattern drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSMBoundaryBoxDisplayData() As DisplayData
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DisplayData

value = instance.IGetSMBoundaryBoxDisplayData()
```

### C#

```csharp
DisplayData IGetSMBoundaryBoxDisplayData()
```

### C++/CLI

```cpp
DisplayData^ IGetSMBoundaryBoxDisplayData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Display data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) of boundary-box sketch of a flat-pattern drawing view

## VBA Syntax

See [View::IGetSMBoundaryBoxDisplayData](ms-its:sldworksapivb6.chm::/sldworks~View~IGetSMBoundaryBoxDisplayData.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSMBoundaryBoxDisplayData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSMBoundaryBoxDisplayData.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
