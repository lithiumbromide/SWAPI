---
title: "GetDatumOriginCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumOriginCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.html"
---

# GetDatumOriginCount Method (IView)

Gets the number of datum origins on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumOriginCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDatumOriginCount()
```

### C#

```csharp
System.int GetDatumOriginCount()
```

### C++/CLI

```cpp
System.int GetDatumOriginCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of datum origins

## VBA Syntax

See [View::GetDatumOriginCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumOriginCount.html).

## Remarks

Call this method before calling [IView::IGetDatumOrigins](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDatumOrigins.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
