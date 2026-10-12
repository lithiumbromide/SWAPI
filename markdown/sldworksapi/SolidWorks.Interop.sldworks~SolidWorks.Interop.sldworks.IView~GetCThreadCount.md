---
title: "GetCThreadCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCThreadCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadCount.html"
---

# GetCThreadCount Method (IView)

Gets the number of cosmetic threads in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCThreadCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetCThreadCount()
```

### C#

```csharp
System.int GetCThreadCount()
```

### C++/CLI

```cpp
System.int GetCThreadCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of cosmetic threads

## VBA Syntax

See [View::GetCThreadCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetCThreadCount.html).

## Remarks

Call this method before calling [IView::IGetCThreads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetCThreads.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
