---
title: "IGetTextFormat Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "IGetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~IGetTextFormat.html"
---

# IGetTextFormat Method (IDrSection)

Gets the text format for the text for this section line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTextFormat() As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As TextFormat

value = instance.IGetTextFormat()
```

### C#

```csharp
TextFormat IGetTextFormat()
```

### C++/CLI

```cpp
TextFormat^ IGetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object for this section line

## VBA Syntax

See [DrSection::IGetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DrSection~IGetTextFormat.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetTextFormat.html)
[IDrSection::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetUseDocTextFormat.html)
[IDrSection::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ISetTextFormat.html)
[IDrSection::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetTextFormat.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
