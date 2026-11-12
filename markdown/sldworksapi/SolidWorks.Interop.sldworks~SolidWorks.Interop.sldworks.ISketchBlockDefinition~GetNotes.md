---
title: "GetNotes Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetNotes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNotes.html"
---

# GetNotes Method (ISketchBlockDefinition)

Gets the notes in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNotes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
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

See [SketchBlockDefinition::GetNotes](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetNotes.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetNoteCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.html)
[ISketchBlockDefinition::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetNotes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
