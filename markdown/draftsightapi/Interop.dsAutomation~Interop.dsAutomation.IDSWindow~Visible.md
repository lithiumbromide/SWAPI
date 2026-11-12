---
title: "Visible Property (IDSWindow)"
project: ""
interface: "IDSWindow"
member: "Visible"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDSWindow~Visible.html"
---

# Visible Property (IDSWindow)

Gets or sets whether to show the DraftSight application or document window.

## Syntax

### Visual Basic

```vb
Property Visible As System.Boolean
```

### C#

```csharp
System.bool Visible {get; set;}
```

### JScript

```
function get,set Visible : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Visible();
__property void set_Visible(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to show the DraftSight application or document window, false to hide it

## Examples

[Get and Set Windows Values (C#)](Get_and_Set_Windows_Values_Example_CSharp.htm)
[Get and Set Windows Values (VB.NET)](Get_and_Set_Windows_Values_Example_VBNET.htm)
[Get and Set Windows Values (VBA)](Get_and_Set_Windows_Values_Example_VBA.htm)

## See Also

[IDSWindow Interface](Interop.dsAutomation~Interop.dsAutomation.IDSWindow.html)
[IDSWindow Members](Interop.dsAutomation~Interop.dsAutomation.IDSWindow_members.html)
[IApplication::Visible Property](Interop.dsAutomation~Interop.dsAutomation.IApplication~Visible.html)

## Availability

DraftSight V1R2.0
