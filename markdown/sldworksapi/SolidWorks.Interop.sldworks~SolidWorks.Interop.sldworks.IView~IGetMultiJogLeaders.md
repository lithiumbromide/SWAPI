---
title: "IGetMultiJogLeaders Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetMultiJogLeaders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetMultiJogLeaders.html"
---

# IGetMultiJogLeaders Method (IView)

Gets all of the multi-jog leaders in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMultiJogLeaders( _
   ByVal NumMultiJogLeader As System.Integer _
) As MultiJogLeader
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumMultiJogLeader As System.Integer
Dim value As MultiJogLeader

value = instance.IGetMultiJogLeaders(NumMultiJogLeader)
```

### C#

```csharp
MultiJogLeader IGetMultiJogLeaders(
   System.int NumMultiJogLeader
)
```

### C++/CLI

```cpp
MultiJogLeader^ IGetMultiJogLeaders(
   System.int NumMultiJogLeader
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumMultiJogLeader`: Number of multi-jog leaders in this drawing view.

### Return Value

- in-process, unmanaged C++: Pointer to an array of [multi-jog leaders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstMultiJogLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstMultiJogLeader.html) and then repeatedly calling [IMultiJogLeader::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader~GetNext.html) to obtain the remaining multi-jog leaders in the drawing view.

Before calling this method, call [IView::GetMultiJogLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetMultiJogLeaderCount.html) to get the value for numMultiJogLeader.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
