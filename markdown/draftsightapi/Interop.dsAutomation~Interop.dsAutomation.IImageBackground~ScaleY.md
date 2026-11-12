---
title: "ScaleY Property (IImageBackground)"
project: ""
interface: "IImageBackground"
member: "ScaleY"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleY.html"
---

# ScaleY Property (IImageBackground)

Gets or sets the y scale of the image for this image background.

## Syntax

### Visual Basic

```vb
Property ScaleY As System.Double
```

### C#

```csharp
System.double ScaleY {get; set;}
```

### JScript

```
function get,set ScaleY : System.double
```

### Managed Extensions for C++

```
__property System.double get_ScaleY();
__property void set_ScaleY(
   System.double value
);
```

### C++/CLI

```cpp
property System.double ScaleY {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

y scale of the image

## Remarks

If [IImageBackground::Position](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~Position.html) is set to [dsImageBackgroundPosition_e](Interop.dsAutomation~Interop.dsAutomation.dsImageBackgroundPosition_e.html).dsImageBackgroundPosition_Stretch, then the y scale is ignored.

## See Also

[IImageBackground Interface](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)
[IImageBackground Members](Interop.dsAutomation~Interop.dsAutomation.IImageBackground_members.html)
[IImageBackground::ScaleX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleX.html)
[IImageBackground::OffsetX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetX.html)
[IImageBackground::OffsetY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetY.html)

## Availability

DraftSight V1R5.0
