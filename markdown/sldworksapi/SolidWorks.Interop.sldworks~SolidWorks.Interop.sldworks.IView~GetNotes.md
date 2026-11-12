---
title: "GetNotes Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.html"
---

# GetNotes Method (IView)

Gets the notes in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNotes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetNotes()
```

### C#

```csharp
System.object GetNotes()
```

### C++/CLI

```cpp
System.Object^ GetNotes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [View::GetNotes](ms-its:sldworksapivb6.chm::/sldworks~View~GetNotes.html).

## Examples

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of notes all at once instead of calling [IView::GetFirstNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstNote.html) and then repeatedly calling [INote::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetNext.html) to obtain the remaining notes on this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetNoteCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNoteCount.html)
[IView::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNotes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
