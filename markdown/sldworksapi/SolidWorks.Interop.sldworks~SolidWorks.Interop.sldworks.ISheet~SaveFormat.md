---
title: "SaveFormat Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SaveFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SaveFormat.html"
---

# SaveFormat Method (ISheet)

Saves the sheet format in the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveFormat( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim FileName As System.String
Dim value As System.Boolean

value = instance.SaveFormat(FileName)
```

### C#

```csharp
System.bool SaveFormat(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool SaveFormat(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name to which to save the sheet format (see Remarks)

### Return Value

True if the sheet format is saved to the specified file, false if not

## VBA Syntax

See [Sheet::SaveFormat](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~SaveFormat.html).

## Examples

[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

## Remarks

You must specify the path, file name, and filename extension to which to save the sheet format. Use .slddrt for the filename extension.

Before calling this method, use [IDrawingDoc::ActivateSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActivateSheet.html) to make the sheet active.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[IDrawingDoc::EditTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.html)
[ISheet::ReloadTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ReloadTemplate.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
