---
title: "SetHeader Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "SetHeader"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html"
---

# SetHeader Method (IPageSetup)

Sets the entire page header.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetHeader( _
   ByVal Left As System.String, _
   ByVal Center As System.String, _
   ByVal Right As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim Left As System.String
Dim Center As System.String
Dim Right As System.String
Dim value As System.Boolean

value = instance.SetHeader(Left, Center, Right)
```

### C#

```csharp
System.bool SetHeader(
   System.string Left,
   System.string Center,
   System.string Right
)
```

### C++/CLI

```cpp
System.bool SetHeader(
   System.String^ Left,
   System.String^ Center,
   System.String^ Right
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Left`: Left-header text
- `Center`: Center-header text
- `Right`: Right-header text

### Return Value

True if the header is successfully changed, false if not

## VBA Syntax

See [PageSetup::SetHeader](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~SetHeader.html).

## Remarks

This method is equivalent to setting [IPageSetup:LeftHeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~LeftHeader.html), [IPageSetup::CenterHeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~CenterHeader.html), and [IPageSetup::RightHeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~RightHeader.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetFooter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html)
[IPageSetup::CenterFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterFooter.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)
[IPageSetup::LeftFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftFooter.html)
[IPageSetup::RightFooter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightFooter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
