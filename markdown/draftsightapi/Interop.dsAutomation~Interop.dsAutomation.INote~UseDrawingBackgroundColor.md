---
title: "UseDrawingBackgroundColor Property (INote)"
project: ""
interface: "INote"
member: "UseDrawingBackgroundColor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~UseDrawingBackgroundColor.html"
---

# UseDrawingBackgroundColor Property (INote)

Gets or sets whether to use the background color of the drawing as the background color of this Note.

## Syntax

### Visual Basic

```vb
Property UseDrawingBackgroundColor As System.Boolean
```

### C#

```csharp
System.bool UseDrawingBackgroundColor {get; set;}
```

### JScript

```
function get,set UseDrawingBackgroundColor : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UseDrawingBackgroundColor();
__property void set_UseDrawingBackgroundColor(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UseDrawingBackgroundColor {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use the background color of the drawing as the background color of this Note, false to use the background fill color specified by [INote::BackgroundFillColor](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundFillColor.html)

## Examples

[Insert Notes with Background Mask (C#)](Insert_Notes_with_Background_Mask_Example_CSharp.htm)
[Insert Notes with Background Mask (VB.NET)](Insert_Notes_with_Background_Mask_Example_VBNET.htm)
[Insert Notes with Background Mask (VBA)](Insert_Notes_with_Background_Mask_Example_VBA.htm)

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::BackgroundBorderOffsetFactor Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundBorderOffsetFactor.html)
[INote::BackgroundMask Property ()](Interop.dsAutomation~Interop.dsAutomation.INote~BackgroundMask.html)

## Availability

DraftSight V1R5.0
