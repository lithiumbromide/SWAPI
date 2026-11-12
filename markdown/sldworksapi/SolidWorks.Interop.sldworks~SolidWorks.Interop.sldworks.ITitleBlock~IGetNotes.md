---
title: "IGetNotes Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "IGetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~IGetNotes.html"
---

# IGetNotes Method (ITitleBlock)

Gets the notes in this title block.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNotes( _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
Dim Count As System.Integer
Dim value As Note

value = instance.IGetNotes(Count)
```

### C#

```csharp
Note IGetNotes(
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetNotes(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of notes in this title block

### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) in this title block

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ITitleBlock::GetNoteCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlock~GetNoteCount.html) before calling this method to get Count.

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0[ITitleBlock::GetNotes Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlock~GetNotes.html)
