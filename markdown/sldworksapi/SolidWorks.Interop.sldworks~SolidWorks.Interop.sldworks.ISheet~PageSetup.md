---
title: "PageSetup Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "PageSetup"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~PageSetup.html"
---

# PageSetup Property (ISheet)

Gets the page setup for this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PageSetup As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Object

value = instance.PageSetup
```

### C#

```csharp
System.object PageSetup {get;}
```

### C++/CLI

```cpp
property System.Object^ PageSetup {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Page setup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup.html)

## VBA Syntax

See [Sheet::PageSetup](ms-its:sldworksapivb6.chm::/sldworks~Sheet~PageSetup.html).

## Remarks

Page setup values are overridden on a sheet by sheet basis.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IPageSetup.html)
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.html)
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.html)
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
