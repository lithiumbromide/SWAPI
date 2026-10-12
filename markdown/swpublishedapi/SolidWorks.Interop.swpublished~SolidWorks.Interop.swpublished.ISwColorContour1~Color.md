---
title: "Color Method (ISwColorContour1)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour1"
member: "Color"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~Color.html"
---

# Color Method (ISwColorContour1)

Gets the color for the specified location on the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Color( _
   ByVal Value As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour1
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

- `Value`: Value that is associated with a location on the model (see **Remarks**)

### Return Value

COLORREF value corresponding to the specified Value

## VBA Syntax

See [SwColorContour1::Color](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour1~Color.html).

## Examples

[Custom Colorize a Model Example (C#)](Custom_Colorize_a_Model_Example_CSharp.htm)
[Custom Colorize a Model Example (VB.NET)](Custom_Colorize_a_Model_Example_VBNET.htm)

## Remarks

When you implement this method, you can return different colors for different locations of the model.

## See Also

[ISwColorContour1 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1.html)
[ISwColorContour1 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1_members.html)
[ISwColorContour1::Value Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~Value.html)

## Availability

SOLIDWORKS 2010 SP05, Revision Number 18.5 and SOLIDWORKS 2011 SP01, Revision Number 19.1
