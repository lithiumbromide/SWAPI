---
title: "UseTwoColors Property (IGradientBackground)"
project: ""
interface: "IGradientBackground"
member: "UseTwoColors"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~UseTwoColors.html"
---

# UseTwoColors Property (IGradientBackground)

Gets or sets which position-dependent colors to use for the gradient background.

## Syntax

### Visual Basic

```vb
Property UseTwoColors As System.Boolean
```

### C#

```csharp
System.bool UseTwoColors {get; set;}
```

### JScript

```
function get,set UseTwoColors : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UseTwoColors();
__property void set_UseTwoColors(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UseTwoColors {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to only use the [top](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~TopColor.html) and [bottom](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~BottomColor.html) colors and ignore the [middle](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground~MiddleColor.html) color, or false to use the top, middle, and bottom colors for the gradient background

## See Also

[IGradientBackground Interface](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground.html)
[IGradientBackground Members](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground_members.html)

## Availability

DraftSight V1R5.0
