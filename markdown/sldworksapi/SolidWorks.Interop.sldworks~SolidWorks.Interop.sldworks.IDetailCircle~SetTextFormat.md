---
title: "SetTextFormat Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetTextFormat.html"
---

# SetTextFormat Method (IDetailCircle)

Sets the text format for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTextFormat( _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean

value = instance.SetTextFormat(UseDoc, TextFormat)
```

### C#

```csharp
System.bool SetTextFormat(
   System.bool UseDoc,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
System.bool SetTextFormat(
   System.bool UseDoc,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to use the local document text format, false to use the text format specified by
  TextFormat
- `TextFormat`: [Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) to use if UseDoc is false

### Return Value

True if the format was set successfully, false if it was not

## VBA Syntax

See [DetailCircle::SetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetTextFormat.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetTextFormat.html)
[IDetailCircle::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetUseDocTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
