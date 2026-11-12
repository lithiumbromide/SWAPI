---
title: "LeftFooter Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "LeftFooter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html"
---

# LeftFooter Property (IPageSetup)

Gets or sets the page footer on the left side of the page.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeftFooter As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.String

instance.LeftFooter = value

value = instance.LeftFooter
```

### C#

```csharp
System.string LeftFooter {get; set;}
```

### C++/CLI

```cpp
property System.String^ LeftFooter {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for footer

## VBA Syntax

See [PageSetup::LeftFooter](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~LeftFooter.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
