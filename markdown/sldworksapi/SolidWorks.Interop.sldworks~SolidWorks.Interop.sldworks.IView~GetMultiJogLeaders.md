---
title: "GetMultiJogLeaders Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetMultiJogLeaders"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.html"
---

# GetMultiJogLeaders Method (IView)

Gets all of the multi-jog leaders in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMultiJogLeaders() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetMultiJogLeaders()
```

### C#

```csharp
System.object GetMultiJogLeaders()
```

### C++/CLI

```cpp
System.Object^ GetMultiJogLeaders();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [multi-jog leaders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)

## VBA Syntax

See [View::GetMultiJogLeaders](ms-its:sldworksapivb6.chm::/sldworks~View~GetMultiJogLeaders.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstMultiJogLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstMultiJogLeader.html) and then repeatedly calling [IMultiJogLeader::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader~GetNext.html) to obtain the remaining multi-jog leaders in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetMultiJogLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaderCount.html)
[IView::IGetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetMultiJogLeaders.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
