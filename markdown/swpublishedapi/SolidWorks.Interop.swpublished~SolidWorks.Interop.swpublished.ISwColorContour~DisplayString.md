---
title: "DisplayString Method (ISwColorContour)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour"
member: "DisplayString"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour~DisplayString.html"
---

# DisplayString Method (ISwColorContour)

Obsolete. Superseded by [ISwColorContour1::DisplayString](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~DisplayString.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayString( _
   ByVal Value As System.Double _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour
Dim Value As System.Double
Dim value As System.String

value = instance.DisplayString(Value)
```

### C#

```csharp
System.string DisplayString(
   System.double Value
)
```

### C++/CLI

```cpp
System.String^ DisplayString(
   System.double Value
)
```

### Parameters

- `Value`: Value associated with the vertex for which to display the string

### Return Value

String to display for the value associated with the vertex

## VBA Syntax

See [SwColorContour::DisplayString](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour~DisplayString.html).

## See Also

[ISwColorContour Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour.html)
[ISwColorContour Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
