---
title: "GetHeaderFooterString Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "GetHeaderFooterString"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html"
---

# GetHeaderFooterString Method (IPageSetup)

Gets the specified standard string that can be used in headers and footers.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeaderFooterString( _
   ByVal WhichOne As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim WhichOne As System.Integer
Dim value As System.String

value = instance.GetHeaderFooterString(WhichOne)
```

### C#

```csharp
System.string GetHeaderFooterString(
   System.int WhichOne
)
```

### C++/CLI

```cpp
System.String^ GetHeaderFooterString(
   System.int WhichOne
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Type of string as defined in [swStandardHeaderFooterPageSetupTexts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardHeaderFooterPageSetupTexts_e.html)

### Return Value

Standard header or footer text

## VBA Syntax

See [PageSetup::GetHeaderFooterString](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~GetHeaderFooterString.html).

## Examples

[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
