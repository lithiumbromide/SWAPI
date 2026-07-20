---
title: "GetFirstMultiJogLeader2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstMultiJogLeader2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader2.html"
---

# GetFirstMultiJogLeader2 Method (IView)

Gets the first multi-jog leader in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstMultiJogLeader2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstMultiJogLeader2()
```

### C#

```csharp
System.object GetFirstMultiJogLeader2()
```

### C++/CLI

```cpp
System.Object^ GetFirstMultiJogLeader2();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[View::GetFirstMultiJogLeader2](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstMultiJogLeader2.html)

.

## Examples

[Get Multi-jog Leader Data (VBA)](Get_Multi-jog_Leader_Data_Example_VB.htm)

[Get Multi-jog Leader Data (VB.NET)](Get_Multi-jog_Leader_Data_Example_VBNET.htm)

[Get Multi-jog Leader Data (C#)](Get_Multi-jog_Leader_Data_Example_CSharp.htm)

## Remarks

This method obsoletes IView::GetFirstMultiJogLeader by supporting inactive sheets.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IMultiJogLeader::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.html)

[IView::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
