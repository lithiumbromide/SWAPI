---
title: "BackgroundBorderOffsetFactor Property (INote)"
project: ""
interface: "INote"
member: "BackgroundBorderOffsetFactor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundBorderOffsetFactor.html"
---

# BackgroundBorderOffsetFactor Property (INote)

Gets or sets the factor by which to offset the border for the background of this Note.

## Syntax

### Visual Basic

```vb
Property BackgroundBorderOffsetFactor As System.Double
```

### C#

```csharp
System.double BackgroundBorderOffsetFactor {get; set;}
```

### JScript

```
function get,set BackgroundBorderOffsetFactor : System.double
```

### Managed Extensions for C++

```
__property System.double get_BackgroundBorderOffsetFactor();
__property void set_BackgroundBorderOffsetFactor(
   System.double value
);
```

### C++/CLI

```cpp
property System.double BackgroundBorderOffsetFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Factor by which to offset the border for the background; valid range is 1 through 5

## Examples

[Insert Notes with Background Mask (C#)](Insert_Notes_with_Background_Mask_Example_CSharp.htm)
[Insert Notes with Background Mask (VB.NET)](Insert_Notes_with_Background_Mask_Example_VBNET.htm)
[Insert Notes with Background Mask (VBA)](Insert_Notes_with_Background_Mask_Example_VBA.htm)

## Remarks

The background fill area is extended by `(INote::BackgroundBorderOffsetFactor - 1) * TextHeight` in all directions. [INote::BackgroundMask](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundMask.html) must be true for INote::BackgroundBorderOffsetFactor to have any effect.

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::BackgroundFillColor Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundFillColor.html)
[INote::UseDrawingBackgroundColor Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~UseDrawingBackgroundColor.html)

## Availability

DraftSight V1R5.0
