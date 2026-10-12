---
title: "GetTextInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetTextInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextInfo.html"
---

# GetTextInfo Method (IDrSection)

Gets the location of the section line text.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Object

value = instance.GetTextInfo()
```

### C#

```csharp
System.object GetTextInfo()
```

### C++/CLI

```cpp
System.Object^ GetTextInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [DrSection::GetTextInfo](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetTextInfo.html).

## Remarks

The section line in a drawing view usually has a piece of text near each end of the line, typically the section view label ([IDrSection::GetLabel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetLabel.html)). The array returned by this method consists of 6 doubles, the (X, Y, Z) origin of one text followed by the (X, Y, Z) origin of the other text. The origin is the upper-left corner of the text.

These values are the same as some of the information in the array returned by [IView::GetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSectionLineInfo2.html). The text information in that array also contains the text height. This method returns an array that does not include that information, but you can get it using [IDrSection::GetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetTextFormat.html) and [ITextFormat::CharHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat~CharHeight.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::IGetTextInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextInfo.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
