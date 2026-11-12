---
title: "GetTextFormat Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetTextFormat.html"
---

# GetTextFormat Method (IDetailCircle)

Gets the text format for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormat() As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As TextFormat

value = instance.GetTextFormat()
```

### C#

```csharp
TextFormat GetTextFormat()
```

### C++/CLI

```cpp
TextFormat^ GetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object

## VBA Syntax

See [DetailCircle::GetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetTextFormat.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetTextFormat.html)
[IDetailCircle::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetUseDocTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
