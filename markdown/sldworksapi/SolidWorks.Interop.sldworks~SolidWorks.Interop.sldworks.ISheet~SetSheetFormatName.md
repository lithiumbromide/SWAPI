---
title: "SetSheetFormatName Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetSheetFormatName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.html"
---

# SetSheetFormatName Method (ISheet)

Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSheetFormatName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetSheetFormatName(Name)
```

### C#

```csharp
System.bool SetSheetFormatName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetSheetFormatName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the sheet format

### Return Value

True if the name of the sheet format is set, false if not

## VBA Syntax

See [Sheet::SetSheetFormatName](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SetSheetFormatName.html).

## Remarks

The name that you specify must:

- be unique in the FeatureManager design tree.
- Not contain any of the SOLIDWORKS reserved special characters.

If either of these conditions is not met, then this method returns false, and the name is not changed. If this sheet does not have a sheet format, this method has no effect.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.html)
[ISheet::GetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.html)
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.html)
[ISheet::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName.html)
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.html)
[ISheet::SheetFormatVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
