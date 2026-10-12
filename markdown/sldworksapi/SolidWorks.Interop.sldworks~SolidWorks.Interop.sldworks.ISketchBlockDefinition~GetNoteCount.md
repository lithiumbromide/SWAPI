---
title: "GetNoteCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetNoteCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.html"
---

# GetNoteCount Method (ISketchBlockDefinition)

Gets the number of notes in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNoteCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
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

Number of notes

## VBA Syntax

See [SketchBlockDefinition::GetNoteCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetNoteCount.html).

## Remarks

Call this method before calling [ISketchBlockDefinition::IGetNotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetNotes.html) to get the size of the array for that method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[SketchBlockDefinition::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNotes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
