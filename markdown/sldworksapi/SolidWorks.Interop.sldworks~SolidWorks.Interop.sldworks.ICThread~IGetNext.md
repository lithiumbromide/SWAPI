---
title: "IGetNext Method (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetNext.html"
---

# IGetNext Method (ICThread)

Gets the next cosmetic thread.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As CThread
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
Dim value As CThread

value = instance.IGetNext()
```

### C#

```csharp
CThread IGetNext()
```

### C++/CLI

```cpp
CThread^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [cosmetic thread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread.html)

## VBA Syntax

See [CThread::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~CThread~IGetNext.html).

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)
[ICThread::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.html)
[IView::GetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.html)
[IView::IGetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCThread.html)
