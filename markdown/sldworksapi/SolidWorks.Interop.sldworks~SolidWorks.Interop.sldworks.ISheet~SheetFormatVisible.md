---
title: "SheetFormatVisible Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SheetFormatVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.html"
---

# SheetFormatVisible Property (ISheet)

Gets or sets whether the sheet format is currently visible in this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetFormatVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Boolean

instance.SheetFormatVisible = value

value = instance.SheetFormatVisible
```

### C#

```csharp
System.bool SheetFormatVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool SheetFormatVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the sheet format is visible, false if not

## VBA Syntax

See [Sheet::SheetFormatVisible](ms-its:sldworksapivb6.chm::/sldworks~Sheet~SheetFormatVisible.html).

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::GetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.html)
[ISheet::SetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
