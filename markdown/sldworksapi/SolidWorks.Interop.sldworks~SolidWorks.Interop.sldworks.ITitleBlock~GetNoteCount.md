---
title: "GetNoteCount Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "GetNoteCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNoteCount.html"
---

# GetNoteCount Method (ITitleBlock)

Gets the number of notes in this title block.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNoteCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
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

Number of notes in this title block

## VBA Syntax

See [TitleBlock::GetNoteCount](ms-its:sldworksapivb6.chm::/sldworks~TitleBlock~GetNoteCount.html).

## Remarks

Call this method before calling [ITitleBlock::IGetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlock~IGetNotes.html) to get the size of the array for that method.

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)
[ITitleBlock::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNotes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
