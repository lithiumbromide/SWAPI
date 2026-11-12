---
title: "GetSMBoundaryBoxDisplayData Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSMBoundaryBoxDisplayData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSMBoundaryBoxDisplayData.html"
---

# GetSMBoundaryBoxDisplayData Method (IView)

Obsolete. Superseded by [IVew::GetSMBoundaryBoxDisplayData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSMBoundaryBoxDisplayData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSMBoundaryBoxDisplayData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSMBoundaryBoxDisplayData()
```

### C#

```csharp
System.object GetSMBoundaryBoxDisplayData()
```

### C++/CLI

```cpp
System.Object^ GetSMBoundaryBoxDisplayData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Display data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) of boundary-box sketch of a flat-pattern drawing view

## VBA Syntax

See [View::GetSMBoundaryBoxDisplayData](ms-its:sldworksapivb6.chm::/sldworks~View~GetSMBoundaryBoxDisplayData.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetSMBoundaryBoxDisplayData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSMBoundaryBoxDisplayData.html)

## Availability

SOLIDWORKS 2011 FCS, Revision 19.0
