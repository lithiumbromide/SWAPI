---
title: "TitleBlock Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "TitleBlock"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock.html"
---

# TitleBlock Property (ISheet)

Gets the title block in this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TitleBlock As TitleBlock
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As TitleBlock

value = instance.TitleBlock
```

### C#

```csharp
TitleBlock TitleBlock {get;}
```

### C++/CLI

```cpp
property TitleBlock^ TitleBlock {
   TitleBlock^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Title block](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITitleBlock.html) in this sheet

## VBA Syntax

See [Sheet::TitleBlock](ms-its:sldworksapivb6.chm::/sldworks~Sheet~TitleBlock.html).

## Examples

[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)

## Remarks

Only one title block can exist in a sheet. This property gets that title block, if it exists.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::TitleBlock Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TitleBlock.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
