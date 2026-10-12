---
title: "GetMultiJogLeaderCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetMultiJogLeaderCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaderCount.html"
---

# GetMultiJogLeaderCount Method (IView)

Gets the number of multi-jog leaders on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMultiJogLeaderCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetMultiJogLeaderCount()
```

### C#

```csharp
System.int GetMultiJogLeaderCount()
```

### C++/CLI

```cpp
System.int GetMultiJogLeaderCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Total number of multi-jog leaders on this drawing view

## VBA Syntax

See [View::GetMultiJogLeaderCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetMultiJogLeaderCount.html).

## Remarks

Call this method before calling [IView::IGetMultiJogLeaders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetMultiJogLeaders.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
