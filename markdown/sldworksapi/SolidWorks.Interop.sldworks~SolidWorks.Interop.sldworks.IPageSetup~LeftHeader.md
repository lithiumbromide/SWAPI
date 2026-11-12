---
title: "LeftHeader Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "LeftHeader"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html"
---

# LeftHeader Property (IPageSetup)

Gets or sets the page header on the left side of the page.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeftHeader As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.String

instance.LeftHeader = value

value = instance.LeftHeader
```

### C#

```csharp
System.string LeftHeader {get; set;}
```

### C++/CLI

```cpp
property System.String^ LeftHeader {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for header

## VBA Syntax

See [PageSetup::LeftHeader](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~LeftHeader.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
