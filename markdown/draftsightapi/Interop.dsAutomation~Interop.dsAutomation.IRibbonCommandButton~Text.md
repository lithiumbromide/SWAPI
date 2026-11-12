---
title: "Text Property (IRibbonCommandButton)"
project: ""
interface: "IRibbonCommandButton"
member: "Text"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton~Text.html"
---

# Text Property (IRibbonCommandButton)

Gets or sets the label of this ribbon command button.

## Syntax

### Visual Basic

```vb
Property Text As System.String
```

### C#

```csharp
System.string Text {get; set;}
```

### JScript

```
function get,set Text : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Text();
__property void set_Text(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Button label text

## Remarks

It is recommended that you set the button labels of only custom ribbon button controls. Do not attempt to change the button labels of system ribbon button controls, as those labels may be used for internal processing.

## See Also

[IRibbonCommandButton Interface](Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton.html)
[IRibbonCommandButton Members](Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton_members.html)

## Availability

DraftSight 2019 SP0
