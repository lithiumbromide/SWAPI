---
title: "IGetFirstNote Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstNote.html"
---

# IGetFirstNote Method (IView)

Gets the first note in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstNote() As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Note

value = instance.IGetFirstNote()
```

### C#

```csharp
Note IGetFirstNote()
```

### C++/CLI

```cpp
Note^ IGetFirstNote();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [View::IGetFirstNote](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstNote.html).

## Remarks

The sheet must be visible. See [ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[INote::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.html)
[INote::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.html)
[IView::GetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.html)
