---
title: "IGetCThreads Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetCThreads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCThreads.html"
---

# IGetCThreads Method (IView)

Gets all of the cosmetic threads on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCThreads( _
   ByVal NumCThread As System.Integer _
) As CThread
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumCThread As System.Integer
Dim value As CThread

value = instance.IGetCThreads(NumCThread)
```

### C#

```csharp
CThread IGetCThreads(
   System.int NumCThread
)
```

### C++/CLI

```cpp
CThread^ IGetCThreads(
   System.int NumCThread
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumCThread`: Total number of cosmetic threads on the drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [cosmetic threads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of cosmetic threads all at once instead of calling [IView::GetFirstCThread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstCThread.html) and then repeatedly calling [ICThread::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~GetNext.html) to obtain the remaining cosmetic threads on the drawing view.

Before calling this method, call [IView::GetCThreadCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCThreadCount.html) to get the value for numCThread.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCThreadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadCount.html)
[IView::GetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.html)
[IView::GetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
