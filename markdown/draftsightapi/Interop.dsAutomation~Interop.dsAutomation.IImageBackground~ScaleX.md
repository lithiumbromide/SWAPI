---
title: "ScaleX Property (IImageBackground)"
project: ""
interface: "IImageBackground"
member: "ScaleX"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleX.html"
---

# ScaleX Property (IImageBackground)

Gets or sets the x scale of the image for this image background.

## Syntax

### Visual Basic

```vb
Property ScaleX As System.Double
```

### C#

```csharp
System.double ScaleX {get; set;}
```

### JScript

```
function get,set ScaleX : System.double
```

### Managed Extensions for C++

```
__property System.double get_ScaleX();
__property void set_ScaleX(
   System.double value
);
```

### C++/CLI

```cpp
property System.double ScaleX {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

x scale of the image

## Remarks

If [IImageBackground::Position](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~Position.html) is set to [dsImageBackgroundPosition_e](Interop.dsAutomation~Interop.dsAutomation.dsImageBackgroundPosition_e.html).dsImageBackgroundPosition_Stretch, then the x scale is ignored.

## See Also

[IImageBackground Interface](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)
[IImageBackground Members](Interop.dsAutomation~Interop.dsAutomation.IImageBackground_members.html)
[IImageBackground::ScaleY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleY.html)
[IImageBackground::OffsetX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetX.html)
[IImageBackground::OffsetY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetY.html)

## Availability

DraftSight V1R5.0
