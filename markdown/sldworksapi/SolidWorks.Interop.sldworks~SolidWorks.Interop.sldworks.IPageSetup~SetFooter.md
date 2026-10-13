---
title: "SetFooter Method (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "SetFooter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetFooter.html"
---

# SetFooter Method (IPageSetup)

Sets the entire page footer.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFooter( _
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

value = instance.SetFooter(Left, Center, Right)
```

### C#

```csharp
System.bool SetFooter(
   System.string Left,
   System.string Center,
   System.string Right
)
```

### C++/CLI

```cpp
System.bool SetFooter(
   System.String^ Left,
   System.String^ Center,
   System.String^ Right
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Left`: Left-footer text
- `Center`: Center-footer text
- `Right`: Right-footer text

### Return Value

True if the footer is successfully changed, false if not

## VBA Syntax

See [PageSetup::SetFooter](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~SetFooter.html).

## Remarks

This method is equivalent to setting [IPageSetup::LeftFooter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~LeftFooter.html), [IPageSetup::CenterFooter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~CenterFooter.html), and [IPageSetup::RightFooter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~RightFooter.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::GetHeaderFooterString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~GetHeaderFooterString.html)
[IPageSetup::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~SetHeader.html)
[IPageSetup::FooterTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~FooterTextFormat.html)
[IPageSetup::HeaderTextFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HeaderTextFormat.html)
[IPageSetup::CenterHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~CenterHeader.html)
[IPageSetup::LeftHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~LeftHeader.html)
[IPageSetup::RightHeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~RightHeader.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
