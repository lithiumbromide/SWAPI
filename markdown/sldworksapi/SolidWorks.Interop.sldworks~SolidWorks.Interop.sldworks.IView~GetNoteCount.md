---
title: "GetNoteCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetNoteCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNoteCount.html"
---

# GetNoteCount Method (IView)

Gets the number notes in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNoteCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetNoteCount()
```

### C#

```csharp
System.int GetNoteCount()
```

### C++/CLI

```cpp
System.int GetNoteCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of notes in this drawing view

## VBA Syntax

See [View::GetNoteCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetNoteCount.html).

## Examples

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetNotes.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.html)
[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
