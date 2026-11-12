---
title: "CenterFooter Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "CenterFooter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html"
---

# CenterFooter Property (IPageSetup)

Gets or sets the page footer in the center of the page.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenterFooter As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.String

instance.CenterFooter = value

value = instance.CenterFooter
```

### C#

```csharp
System.string CenterFooter {get; set;}
```

### C++/CLI

```cpp
property System.String^ CenterFooter {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for the footer

## VBA Syntax

See [PageSetup::CenterFooter](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~CenterFooter.html).

## Examples

[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
