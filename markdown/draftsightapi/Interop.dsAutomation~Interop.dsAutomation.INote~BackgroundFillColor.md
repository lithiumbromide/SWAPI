---
title: "BackgroundFillColor Property (INote)"
project: ""
interface: "INote"
member: "BackgroundFillColor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundFillColor.html"
---

# BackgroundFillColor Property (INote)

Gets or sets the background fill Color of this Note.

## Syntax

### Visual Basic

```vb
Property BackgroundFillColor As Color
```

### C#

```csharp
Color BackgroundFillColor {get; set;}
```

### JScript

```
function get,set BackgroundFillColor : Color
```

### Managed Extensions for C++

```
__property Color* get_BackgroundFillColor();
__property void set_BackgroundFillColor(
   Color* value
);
```

### C++/CLI

```cpp
property Color^ BackgroundFillColor {
   Color^ get();
   void set (    Color^ value);
}
```

### Property Value

Background fill [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Examples

[Insert Notes with Background Mask (C#)](Insert_Notes_with_Background_Mask_Example_CSharp.htm)
[Insert Notes with Background Mask (VB.NET)](Insert_Notes_with_Background_Mask_Example_VBNET.htm)
[Insert Notes with Background Mask (VBA)](Insert_Notes_with_Background_Mask_Example_VBA.htm)

## Remarks

[INote::BackgroundMask](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundMask.html) must be true for INote::BackgroundFillColor to have any effect.

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::BackgroundBorderOffsetFactor Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundBorderOffsetFactor.html)
[INote::UseDrawingBackgroundColor Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~UseDrawingBackgroundColor.html)

## Availability

DraftSight V1R5.0
