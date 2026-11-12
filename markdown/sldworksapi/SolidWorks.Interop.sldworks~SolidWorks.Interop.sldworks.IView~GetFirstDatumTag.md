---
title: "GetFirstDatumTag Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstDatumTag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumTag.html"
---

# GetFirstDatumTag Method (IView)

Gets the first datum tag in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDatumTag() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstDatumTag()
```

### C#

```csharp
System.object GetFirstDatumTag()
```

### C++/CLI

```cpp
System.Object^ GetFirstDatumTag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [datum tag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html)

## VBA Syntax

See [View::GetFirstDatumTag](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstDatumTag.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetFirstDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDatumTag.html)
[IDatumTag::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetNext.html)
[IDatumTag::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetNext.html)
[IView::IGetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTags.html)
[IView::GetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags.html)
