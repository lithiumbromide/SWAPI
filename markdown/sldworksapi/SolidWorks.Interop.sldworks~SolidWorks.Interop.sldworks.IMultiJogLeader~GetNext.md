---
title: "GetNext Method (IMultiJogLeader)"
project: "SOLIDWORKS API Help"
interface: "IMultiJogLeader"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.html"
---

# GetNext Method (IMultiJogLeader)

Gets the next leader in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMultiJogLeader
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [leader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader.html)

## VBA Syntax

See [MultiJogLeader::GetNext](ms-its:sldworksapivb6.chm::/sldworks~MultiJogLeader~GetNext.html).

## See Also

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.html)
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.html)
[IMultiJogLeader::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetNext.html)
[IView::IGetFirstMultiJogLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstMultiJogLeader.html)
[IView::GetFirstMultiJogLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
