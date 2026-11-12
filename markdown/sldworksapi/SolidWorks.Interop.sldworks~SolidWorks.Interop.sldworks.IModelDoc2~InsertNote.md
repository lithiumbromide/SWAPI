---
title: "InsertNote Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNote.html"
---

# InsertNote Method (IModelDoc2)

Inserts a note in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNote( _
   ByVal Text As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Text As System.String
Dim value As System.Object

value = instance.InsertNote(Text)
```

### C#

```csharp
System.object InsertNote(
   System.string Text
)
```

### C++/CLI

```cpp
System.Object^ InsertNote(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text string or symbol for the note (see **Remarks**)

### Return Value

Newly created [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDoc2::InsertNote](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertNote.html).

## Examples

[Insert Note (VBA)](Insert_a_Note_Example_VB.htm)
[Create Block Definition and Insert Block Instance (VBA)](Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm)
[Create Block Definition and Insert Block Instance (C#)](Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm)
[Create Block Definition and Insert Block Instance (VB.NET)](Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm)

## Remarks

If you use a symbol in Text, it must be formatted as:

<`LibraryName-SymbolName`>

where `LibraryName` and `SymbolName` are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.**

NOTE: You must include the right- and left-angle brackets and separate `LibraryName` and `SymbolName` with a hyphen; for example, <MOD-DEG>.

The leader attachment points for the new note come from the selections made before calling this method. The initial location of the note will be near the selection location. If there are no selections, the note:

- Does not have a leader
- Is free standing
- Is at the origin of the model or drawing

This method creates a default note. To adjust the display characteristics of this note, you should use the pointer that is returned by this method to access the properties and get and set methods of the Note object, such as [INote::SetBalloon](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~SetBalloon.html), [INote::Angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~Angle.html), and [INote::LockPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~LockPosition.html). Use [INote::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetAnnotation.html) or [INote::IGetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetAnnotation.html) to retrieve the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[IModelDoc2::InsertNewNote3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.html)
[IModelDoc2::IInsertNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertNote.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
