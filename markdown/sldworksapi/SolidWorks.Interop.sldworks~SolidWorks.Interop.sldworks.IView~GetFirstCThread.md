---
title: "GetFirstCThread Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstCThread"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.html"
---

# GetFirstCThread Method (IView)

Gets the first cosmetic thread in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCThread() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstCThread()
```

### C#

```csharp
System.object GetFirstCThread()
```

### C++/CLI

```cpp
System.Object^ GetFirstCThread();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [cosmetic thread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread.html)

## VBA Syntax

See [View::GetFirstCThread](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstCThread.html).

## Examples

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCThread.html)
[ICThread::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.html)
[ICThread::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetNext.html)
[IView::IGetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCThreads.html)
[IView::GetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.html)
