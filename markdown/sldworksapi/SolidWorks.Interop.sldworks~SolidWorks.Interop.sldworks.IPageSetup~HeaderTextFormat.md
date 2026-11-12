---
title: "HeaderTextFormat Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "HeaderTextFormat"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html"
---

# HeaderTextFormat Property (IPageSetup)

Gets or sets the text format for the page header.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HeaderTextFormat As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As TextFormat

value = instance.HeaderTextFormat
```

### C#

```csharp
TextFormat HeaderTextFormat {get;}
```

### C++/CLI

```cpp
property TextFormat^ HeaderTextFormat {
   TextFormat^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) for header

## VBA Syntax

See [PageSetup::HeaderTextFormat](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~HeaderTextFormat.html).

## Remarks

The following line of code to change the font of the header text to Arial:

PageSetup.HeaderTextFormat.TypeFaceName = "Arial"

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
