---
title: "CenterHeader Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "CenterHeader"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html"
---

# CenterHeader Property (IPageSetup)

Gets or sets the page header in the center of the page.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenterHeader As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.String

instance.CenterHeader = value

value = instance.CenterHeader
```

### C#

```csharp
System.string CenterHeader {get; set;}
```

### C++/CLI

```cpp
property System.String^ CenterHeader {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for header

## VBA Syntax

See [PageSetup::CenterHeader](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~CenterHeader.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
