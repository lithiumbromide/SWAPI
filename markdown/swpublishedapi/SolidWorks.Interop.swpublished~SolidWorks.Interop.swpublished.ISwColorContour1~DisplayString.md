---
title: "DisplayString Method (ISwColorContour1)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour1"
member: "DisplayString"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~DisplayString.html"
---

# DisplayString Method (ISwColorContour1)

Gets the string to display for the specified location on the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayString( _
   ByVal Value As System.Double _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour1
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

- `Value`: Value that is associated with a location on the model (see **Remarks**)

### Return Value

String to display for the specified Value

## VBA Syntax

See [SwColorContour1::DisplayString](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour1~DisplayString.html).

## Examples

[Custom Colorize a Model Example (C#)](Custom_Colorize_a_Model_Example_CSharp.htm)
[Custom Colorize a Model Example (VB.NET)](Custom_Colorize_a_Model_Example_VBNET.htm)

## Remarks

When you implement this method, you can return different strings for different locations of the model.

## See Also

[ISwColorContour1 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1.html)
[ISwColorContour1 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1_members.html)
[ISwColorContour1::Value Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~Value.html)

## Availability

SOLIDWORKS 2010 SP05, Revision Number 18.5 and SOLIDWORKS 2011 SP01, Revision Number 19.1
