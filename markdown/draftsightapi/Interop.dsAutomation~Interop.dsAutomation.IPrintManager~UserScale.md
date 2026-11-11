---
title: "UserScale Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "UserScale"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UserScale.html"
---

# UserScale Property (IPrintManager)

Gets or sets whether to use a user-defined scale when printing.

## Syntax

### Visual Basic

```vb
Property UserScale As System.Boolean
```

### C#

```csharp
System.bool UserScale {get; set;}
```

### JScript

```
function get,set UserScale : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UserScale();
__property void set_UserScale(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UserScale {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to use a user-defined scale for printing, false to not

## Remarks

If this property is set to true, use [IPrintManager::SetUserScaleValue](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetUserScaleValue.html) to set the user-defined scale for printing.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::ScaleToFit Property](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ScaleToFit.html)

## Availability

DraftSight V1R1
