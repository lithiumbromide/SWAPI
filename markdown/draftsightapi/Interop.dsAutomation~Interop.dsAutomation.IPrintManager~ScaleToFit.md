---
title: "ScaleToFit Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "ScaleToFit"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ScaleToFit.html"
---

# ScaleToFit Property (IPrintManager)

Gets or sets whether to scale the printout to fit the paper.

## Syntax

### Visual Basic

```vb
Property ScaleToFit As System.Boolean
```

### C#

```csharp
System.bool ScaleToFit {get; set;}
```

### JScript

```
function get,set ScaleToFit : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_ScaleToFit();
__property void set_ScaleToFit(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool ScaleToFit {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to scale the printout to fit the paper, false to use a different scale

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

If this property is set to false, use:

- [IPrintManager::SetStandardScale](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetStandardScale.html)

- or -

- [IPrintManager::UserScale](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UserScale.html) and [IPrintManager::SetUserScaleValue](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html)

to specify the print scale.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
