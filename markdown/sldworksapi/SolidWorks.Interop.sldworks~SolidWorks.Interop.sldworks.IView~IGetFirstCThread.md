---
title: "IGetFirstCThread Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstCThread"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCThread.html"
---

# IGetFirstCThread Method (IView)

Gets the first cosmetic thread in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstCThread() As CThread
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As CThread

value = instance.IGetFirstCThread()
```

### C#

```csharp
CThread IGetFirstCThread()
```

### C++/CLI

```cpp
CThread^ IGetFirstCThread();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [cosmetic thread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread.html)

## VBA Syntax

See [View::IGetFirstCThread](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstCThread.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.html)
[ICThread::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.html)
[ICThread::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetNext.html)
