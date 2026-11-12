---
title: "NeedsUpdate Method (ISwColorContour1)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour1"
member: "NeedsUpdate"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~NeedsUpdate.html"
---

# NeedsUpdate Method (ISwColorContour1)

Specifies whether the SOLIDWORKS software refreshes the color and display.

## Syntax

### Visual Basic (Declaration)

```vb
Function NeedsUpdate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour1
Dim value As System.Boolean

value = instance.NeedsUpdate()
```

### C#

```csharp
System.bool NeedsUpdate()
```

### C++/CLI

```cpp
System.bool NeedsUpdate();
```

### Return Value

True if the colors defined are not up-to-date, false if they are

## VBA Syntax

See [SwColorContour1::NeedsUpdate](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour1~NeedsUpdate.html).

## Examples

[Custom Colorize a Model Example (C#)](Custom_Colorize_a_Model_Example_CSharp.htm)
[Custom Colorize a Model Example (VB.NET)](Custom_Colorize_a_Model_Example_VBNET.htm)

## See Also

[ISwColorContour1 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1.html)
[ISwColorContour1 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1_members.html)

## Availability

SOLIDWORKS 2010 SP05, Revision Number 18.5 and SOLIDWORKS 2011 SP01, Revision Number 19.1
