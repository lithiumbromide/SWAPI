---
title: "Value Method (ISwColorContour)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour"
member: "Value"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour~Value.html"
---

# Value Method (ISwColorContour)

Obsolete. Superseded by [ISwColorContour1::Value](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~Value.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Value( _
   ByVal face As System.Object, _
   ByRef vertexCoords As System.Single, _
   ByRef normalCoords As System.Single, _
   ByRef Value As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour
Dim face As System.Object
Dim vertexCoords As System.Single
Dim normalCoords As System.Single
Dim Value As System.Double
Dim value As System.Integer

value = instance.Value(face, vertexCoords, normalCoords, Value)
```

### C#

```csharp
System.int Value(
   System.object face,
   ref System.float vertexCoords,
   ref System.float normalCoords,
   out System.double Value
)
```

### C++/CLI

```cpp
System.int Value(
   System.Object^ face,
   System.float% vertexCoords,
   System.float% normalCoords,
   [Out] System.double Value
)
```

### Parameters

- `face`: Face on the model
- `vertexCoords`: Array of vertex coordinates (x, y, z) to which to color
- `normalCoords`: Array of normal coordinates (x, y, z) to which to color
- `Value`: Value defined by the add-in to display

### Return Value

COLORREF value that represents value

## VBA Syntax

See [SwColorContour::Value](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour~Value.html).

## See Also

[ISwColorContour Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour.html)
[ISwColorContour Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
