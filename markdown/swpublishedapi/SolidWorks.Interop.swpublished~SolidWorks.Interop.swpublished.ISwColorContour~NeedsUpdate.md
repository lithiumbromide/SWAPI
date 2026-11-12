---
title: "NeedsUpdate Method (ISwColorContour)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour"
member: "NeedsUpdate"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour~NeedsUpdate.html"
---

# NeedsUpdate Method (ISwColorContour)

Obsolete. Superseded by [ISwColorContour1::NeedsUpdate](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~NeedsUpdate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function NeedsUpdate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour
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

True if the colors defined by the add-in are not up-to-date, false if they are

## VBA Syntax

See [SwColorContour::NeedsUpdate](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour~NeedsUpdate.html).

## See Also

[ISwColorContour Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour.html)
[ISwColorContour Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
