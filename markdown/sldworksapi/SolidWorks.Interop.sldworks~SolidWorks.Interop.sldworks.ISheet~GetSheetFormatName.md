---
title: "GetSheetFormatName Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetSheetFormatName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.html"
---

# GetSheetFormatName Method (ISheet)

Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetFormatName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.String

value = instance.GetSheetFormatName()
```

### C#

```csharp
System.string GetSheetFormatName()
```

### C++/CLI

```cpp
System.String^ GetSheetFormatName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the sheet format

## VBA Syntax

See [Sheet::GetSheetFormatName](ms-its:sldworksapivb6.chm::/sldworks~Sheet~GetSheetFormatName.html).

## Remarks

If the sheet does not have a sheet format, an empty string is returned.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.html)
[ISheet::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName.html)
[ISheet::SetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.html)
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)
[ISheet::SheetFormatVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
