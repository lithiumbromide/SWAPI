---
title: "GetFirstNote Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.html"
---

# GetFirstNote Method (IView)

Obsolete. Superseded by

[IView::GetFirstNote2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstNote() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstNote()
```

### C#

```csharp
System.object GetFirstNote()
```

### C++/CLI

```cpp
System.Object^ GetFirstNote();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See

[View::GetFirstNote](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstNote.html)

.

## Remarks

The sheet must be visible. See[ISheet::SheetFormatVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet~SheetFormatVisible.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::IGetFirstNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstNote.html)

[INote::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.html)

[INote::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.html)
