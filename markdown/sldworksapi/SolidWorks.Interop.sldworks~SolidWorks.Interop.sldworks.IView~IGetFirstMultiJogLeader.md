---
title: "IGetFirstMultiJogLeader Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstMultiJogLeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstMultiJogLeader.html"
---

# IGetFirstMultiJogLeader Method (IView)

Gets the first multi-jog leader in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstMultiJogLeader() As MultiJogLeader
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As MultiJogLeader

value = instance.IGetFirstMultiJogLeader()
```

### C#

```csharp
MultiJogLeader IGetFirstMultiJogLeader()
```

### C++/CLI

```cpp
MultiJogLeader^ IGetFirstMultiJogLeader();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [multi-jog leader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)

## VBA Syntax

See [View::IGetFirstMultiJogLeader](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstMultiJogLeader.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstMultiJogLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader.html)
[IMultiJogLeader::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.html)
[IMultiJogLeader::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
