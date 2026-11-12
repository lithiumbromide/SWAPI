---
title: "OffsetX Property (IImageBackground)"
project: ""
interface: "IImageBackground"
member: "OffsetX"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetX.html"
---

# OffsetX Property (IImageBackground)

Gets or sets the x offset of the image.

## Syntax

### Visual Basic

```vb
Property OffsetX As System.Double
```

### C#

```csharp
System.double OffsetX {get; set;}
```

### JScript

```
function get,set OffsetX : System.double
```

### Managed Extensions for C++

```
__property System.double get_OffsetX();
__property void set_OffsetX(
   System.double value
);
```

### C++/CLI

```cpp
property System.double OffsetX {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

x offset of the image

## Remarks

If [IImageBackground::Position](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~Position.html) is set to [dsImageBackgroundPosition_e](Interop.dsAutomation~Interop.dsAutomation.dsImageBackgroundPosition_e.html).dsImageBackgroundPosition_Stretch, then the x offset is ignored.

## See Also

[IImageBackground Interface](Interop.dsAutomation~Interop.dsAutomation.IImageBackground.html)
[IImageBackground Members](Interop.dsAutomation~Interop.dsAutomation.IImageBackground_members.html)
[IImageBackground::OffsetY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~OffsetY.html)
[IImageBackground::ScaleX Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleX.html)
[IImageBackground::ScaleY Property ()](Interop.dsAutomation~Interop.dsAutomation.IImageBackground~ScaleY.html)

## Availability

DraftSight V1R5.0
