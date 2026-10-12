---
title: "IPageSetup Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "IPageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.html"
---

# IPageSetup Property (ISheet)

Gets the page setup for this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IPageSetup As PageSetup
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As PageSetup

value = instance.IPageSetup
```

### C#

```csharp
PageSetup IPageSetup {get;}
```

### C++/CLI

```cpp
property PageSetup^ IPageSetup {
   PageSetup^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Page setup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)

## VBA Syntax

See [Sheet::IPageSetup](ms-its:sldworksapivb6.chm::/sldworks~Sheet~IPageSetup.html).

## Remarks

Page setup values are overridden on a sheet by sheet basis.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
