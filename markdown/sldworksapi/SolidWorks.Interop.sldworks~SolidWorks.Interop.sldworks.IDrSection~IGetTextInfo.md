---
title: "IGetTextInfo Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetTextInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextInfo.html"
---

# IGetTextInfo Method (IDrSection)

Gets the location of the section line text.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextInfo() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Double

value = instance.IGetTextInfo()
```

### C#

```csharp
System.double IGetTextInfo()
```

### C++/CLI

```cpp
System.double IGetTextInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The section line in a drawing view usually has a piece of text near each end of the line, typically the section view label ([IDrSection::GetLabel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~GetLabel.html)). The array returned by this method consists of 6 doubles, the (X, Y, Z) origin of one text followed by the (X, Y, Z) origin of the other text. The origin is the upper-left corner of the text.

These values are the same as some of the information in the array returned by [IView::IGetSectionLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSectionLineInfo2.html). The text information in that array also contains the text height. This method returns an array that does not include that information, but you can get it using [IDrSection::IGetTextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection~IGetTextFormat.html) and [ITextFormat::CharHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat~CharHeight.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetTextInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextInfo.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
