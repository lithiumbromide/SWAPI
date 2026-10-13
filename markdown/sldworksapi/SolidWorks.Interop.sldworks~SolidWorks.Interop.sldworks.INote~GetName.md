---
title: "GetName Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetName.html"
---

# GetName Method (INote)

Gets the name of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.String

value = instance.GetName()
```

### C#

```csharp
System.string GetName()
```

### C++/CLI

```cpp
System.String^ GetName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the note

## VBA Syntax

See [Note::GetName](ms-its:sldworksapivb6.chm::/sldworks~Note~GetName.html).

## Examples

[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)
[Get Note By Name (VBA)](Get_Note_By_Name_Example_VB.htm)
[Remove Hyperlink From Note in Drawing (VBA)](Remove_Hyperlink_from_Note_in_Drawing_Example_VB.htm)
[Set Note Name (VBA)](Set_Note_Name_Example.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

## Remarks

This method returns an empty string if the note is part of a block.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetName.html)
