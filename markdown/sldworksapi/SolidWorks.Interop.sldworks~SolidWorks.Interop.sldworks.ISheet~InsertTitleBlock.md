---
title: "InsertTitleBlock Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "InsertTitleBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertTitleBlock.html"
---

# InsertTitleBlock Method (ISheet)

Inserts a title block into this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertTitleBlock( _
   ByVal Notes As System.Object _
) As TitleBlock
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Notes As System.Object
Dim value As TitleBlock

value = instance.InsertTitleBlock(Notes)
```

### C#

```csharp
TitleBlock InsertTitleBlock(
   System.object Notes
)
```

### C++/CLI

```cpp
TitleBlock^ InsertTitleBlock(
   System.Object^ Notes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Notes`: Array of notes or nothing (see **Remarks**)

### Return Value

[Title block](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlock.html)

## VBA Syntax

See [Sheet::InsertTitleBlock](ms-its:sldworksapivb6.chm::/sldworks~Sheet~InsertTitleBlock.html).

## Examples

[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

## Remarks

The Notes parameter can contain one or more more notes or nothing. If the Notes parameter contains a note, or notes, then the note, or notes, is expected to be a Dispatch pointer, or pointers, to the [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object, or objects, to include as part of the title block being created.

Only one title block can exist in a sheet.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::TitleBlock Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
