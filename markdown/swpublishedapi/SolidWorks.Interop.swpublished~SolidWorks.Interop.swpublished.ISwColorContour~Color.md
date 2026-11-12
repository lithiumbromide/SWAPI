---
title: "Color Method (ISwColorContour)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour"
member: "Color"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour~Color.html"
---

# Color Method (ISwColorContour)

Obsolete. Superseded by [ISwColorContour1::Color](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~Color.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Color( _
   ByVal Value As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour
Dim Value As System.Double
Dim value As System.Integer

value = instance.Color(Value)
```

### C#

```csharp
System.int Color(
   System.double Value
)
```

### C++/CLI

```cpp
System.int Color(
   System.double Value
)
```

### Parameters

- `Value`: Value that corresponds to the color

### Return Value

COLORREF value that represents value

## VBA Syntax

See [SwColorContour::Color](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour~Color.html).

## See Also

[ISwColorContour Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour.html)
[ISwColorContour Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
