---
title: "IGetFirstGTOL Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstGTOL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstGTOL.html"
---

# IGetFirstGTOL Method (IView)

Gets the first geometric tolerance in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstGTOL() As Gtol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Gtol

value = instance.IGetFirstGTOL()
```

### C#

```csharp
Gtol IGetFirstGTOL()
```

### C++/CLI

```cpp
Gtol^ IGetFirstGTOL();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [GTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See [View::IGetFirstGTOL](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstGTOL.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstGTOL.html)
[IGtol::GetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetNextGTOL.html)
[IGtol::IGetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetNextGTOL.html)
