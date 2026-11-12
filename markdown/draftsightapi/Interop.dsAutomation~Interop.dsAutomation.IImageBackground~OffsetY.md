---
title: "OffsetY Property (IImageBackground)"
project: ""
interface: "IImageBackground"
member: "OffsetY"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetY.html"
---

# OffsetY Property (IImageBackground)

Gets or sets the y offset of the image for the image background.

## Syntax

### Visual Basic

```vb
Property OffsetY As System.Double
```

### C#

```csharp
System.double OffsetY {get; set;}
```

### JScript

```
function get,set OffsetY : System.double
```

### Managed Extensions for C++

```
__property System.double get_OffsetY();
__property void set_OffsetY(
   System.double value
);
```

### C++/CLI

```cpp
property System.double OffsetY {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

y offset of the image

## Remarks

If [IImageBackground::Position](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~Position.html) is set to [dsImageBackgroundPosition_e](Interop.dsAutomation~Interop.dsAutomation.dsImageBackgroundPosition_e.html).dsImageBackgroundPosition_Stretch, then the y offset is ignored.

## See Also

[IImageBackground Interface](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)
[IImageBackground Members](Interop.dsAutomation~Interop.dsAutomation.IImageBackground_members.html)
[IImageBackground::OffsetX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetX.html)
[IImageBackground::ScaleX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleX.html)
[IImageBackground::ScaleY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleY.html)

## Availability

DraftSight V1R5.0
