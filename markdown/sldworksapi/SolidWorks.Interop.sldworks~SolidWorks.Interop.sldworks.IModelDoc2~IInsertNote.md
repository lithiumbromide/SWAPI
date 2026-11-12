---
title: "IInsertNote Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IInsertNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertNote.html"
---

# IInsertNote Method (IModelDoc2)

Inserts a note in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertNote( _
   ByVal Text As System.String _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Text As System.String
Dim value As Note

value = instance.IInsertNote(Text)
```

### C#

```csharp
Note IInsertNote(
   System.string Text
)
```

### C++/CLI

```cpp
Note^ IInsertNote(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text string or symbol for the note (see **Remarks**)

### Return Value

Newly created [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDoc2::IInsertNote](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IInsertNote.html).

## Remarks

If you use a symbol in Text, it must be formatted as:

<`LibraryName-SymbolName`>

where `LibraryName` and `SymbolName` are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.**

NOTE: You must include the right- and left-angle brackets and separate `LibraryName` and `SymbolName` with a hyphen; for example, <MOD-DEG>.

The leader attachment points for the new note come from the selections made before calling this method. The initial location of the note will be near the selection location. If there are no selections, the note:

- Does not have a leader
- Is free standing
- Is at the origin of the model or drawing

This method creates a default note. To adjust the display characteristics of this note, you should use the pointer that is returned by this method to access the properties and get and set methods of the Note object, such as [INote::SetBalloon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~SetBalloon.html) and [INote::Angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~Angle.html). Use [INote::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetAnnotation.html) or [INote::IGetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetAnnotation.html) to retrieve the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNote.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
