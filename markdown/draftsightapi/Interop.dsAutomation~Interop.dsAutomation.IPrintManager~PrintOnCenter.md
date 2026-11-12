---
title: "PrintOnCenter Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PrintOnCenter"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintOnCenter.html"
---

# PrintOnCenter Property (IPrintManager)

Gets or sets whether to use same-size margins at the top, bottom, left, and right for print offset.

## Syntax

### Visual Basic

```vb
Property PrintOnCenter As System.Boolean
```

### C#

```csharp
System.bool PrintOnCenter {get; set;}
```

### JScript

```
function get,set PrintOnCenter : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_PrintOnCenter();
__property void set_PrintOnCenter(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool PrintOnCenter {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to to use same-size margins at the top, bottom, left, and right for print offset, false to not

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

To specify margins of different sizes for print offset, set this property to false and use [IPrintManager::SetPrintOffset](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~SetPrintOffset.html) to set the size of the margins.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)
[IPrintManager::GetPrintOffset Method](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~GetPrintOffset.html)

## Availability

DraftSight V1R1
