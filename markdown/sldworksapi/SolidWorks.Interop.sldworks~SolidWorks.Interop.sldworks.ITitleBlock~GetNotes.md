---
title: "GetNotes Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "GetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNotes.html"
---

# GetNotes Method (ITitleBlock)

Gets the notes in this title block.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNotes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
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

Array of [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) in this title block

## VBA Syntax

See [TitleBlock::GetNotes](ms-its:sldworksapivb6.chm::/sldworks~TitleBlock~GetNotes.html).

## Examples

[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)
[ITitleBlock::GetNoteCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNoteCount.html)
[ITitleBlock::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~IGetNotes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
