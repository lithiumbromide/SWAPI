---
title: "IGetNotes Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNotes.html"
---

# IGetNotes Method (IView)

Gets the notes in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNotes( _
   ByVal NumberOfNotes As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumberOfNotes As System.Integer
Dim value As Note

value = instance.IGetNotes(NumberOfNotes)
```

### C#

```csharp
Note IGetNotes(
   System.int NumberOfNotes
)
```

### C++/CLI

```cpp
Note^ IGetNotes(
   System.int NumberOfNotes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumberOfNotes`: Number of notes in this drawing view

### Return Value

in-process, unmanaged C++: Pointer to an array of [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of notes all at once instead of calling [IView::GetFirstNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstNote.html) and then repeatedly calling [INote::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetNext.html) to obtain the remaining notes on this drawing view.

Call [IView::GetNoteCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetNoteCount.html) before calling this method to get NumberOfNotes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
