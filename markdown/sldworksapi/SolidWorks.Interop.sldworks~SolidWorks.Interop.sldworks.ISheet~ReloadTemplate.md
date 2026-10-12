---
title: "ReloadTemplate Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "ReloadTemplate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ReloadTemplate.html"
---

# ReloadTemplate Method (ISheet)

Reloads the sheet format from the original sheet format template.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReloadTemplate( _
   ByVal KeepNoteChanges As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim KeepNoteChanges As System.Boolean
Dim value As System.Integer

value = instance.ReloadTemplate(KeepNoteChanges)
```

### C#

```csharp
System.int ReloadTemplate(
   System.bool KeepNoteChanges
)
```

### C++/CLI

```cpp
System.int ReloadTemplate(
   System.bool KeepNoteChanges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `KeepNoteChanges`: True to keep note modifications made to the sheet format and reload all other elements from the original sheet format template, false to reload all elements from the original sheet format template and discard any note modifications made to the sheet format

### Return Value

Status as defined in [swReloadTemplateResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReloadTemplateResult_e.html)

## VBA Syntax

See [Sheet::ReloadTemplate](ms-its:sldworksapivb6.chm::/sldworks~Sheet~ReloadTemplate.html).

## Examples

[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

## Remarks

If new notes are added or existing notes modified or deleted on the sheet format, then specifying true for KeepNoteChanges:

- adds the new notes to the sheet format template, but does not duplicate the new notes on the sheet format.
- restores any deleted notes from the sheet format template on the sheet format.
- duplicates all other notes in their original position from the sheet format template on the sheet format.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[IDrawingDoc::EditTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.html)
[ISheet::SaveFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SaveFormat.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
