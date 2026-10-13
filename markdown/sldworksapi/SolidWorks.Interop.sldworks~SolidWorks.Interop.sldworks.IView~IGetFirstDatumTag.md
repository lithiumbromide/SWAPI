---
title: "IGetFirstDatumTag Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstDatumTag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDatumTag.html"
---

# IGetFirstDatumTag Method (IView)

Gets the first datum tag in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstDatumTag() As DatumTag
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DatumTag

value = instance.IGetFirstDatumTag()
```

### C#

```csharp
DatumTag IGetFirstDatumTag()
```

### C++/CLI

```cpp
DatumTag^ IGetFirstDatumTag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [datum tag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html)

## VBA Syntax

See [View::IGetFirstDatumTag](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstDatumTag.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDatumTag::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetNext.html)
[IDatumTag::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.html)
[IView::GetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.html)
