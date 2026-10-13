---
title: "GetFirstGTOL Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstGTOL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstGTOL.html"
---

# GetFirstGTOL Method (IView)

Gets the first geometric tolerance in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstGTOL() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstGTOL()
```

### C#

```csharp
System.object GetFirstGTOL()
```

### C++/CLI

```cpp
System.Object^ GetFirstGTOL();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [GTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See [View::GetFirstGTOL](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstGTOL.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IGtol::GetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetNextGTOL.html)
[IGtol::IGetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetNextGTOL.html)
[IView::IGetFirstGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstGTOL.html)
[IView::IGetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.html)
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.html)
