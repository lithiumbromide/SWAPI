---
title: "CustomIconPath Property (IInterfaceFiles)"
project: ""
interface: "IInterfaceFiles"
member: "CustomIconPath"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles~CustomIconPath.html"
---

# CustomIconPath Property (IInterfaceFiles)

Gets or sets where to search for custom icon files for toolbars and menus.

## Syntax

### Visual Basic

```vb
Property CustomIconPath As System.String
```

### C#

```csharp
System.string CustomIconPath {get; set;}
```

### JScript

```
function get,set CustomIconPath : System.String
```

### Managed Extensions for C++

```
__property System.string* get_CustomIconPath();
__property void set_CustomIconPath(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ CustomIconPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path where to search for custom icon files for toolbars and menus

## Examples

See the [IInterfaceFiles](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html) examples.

## Remarks

The filename extension for custom icon files is **.xml**.

## See Also

[IInterfaceFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html)
[IInterfaceFiles Members](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles_members.html)
[IApplication::CreateUserCommand Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateUserCommand.html)

## Availability

DraftSight V1R5.0
