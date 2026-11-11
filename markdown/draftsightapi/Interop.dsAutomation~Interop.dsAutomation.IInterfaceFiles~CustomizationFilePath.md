---
title: "CustomizationFilePath Property (IInterfaceFiles)"
project: ""
interface: "IInterfaceFiles"
member: "CustomizationFilePath"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles~CustomizationFilePath.html"
---

# CustomizationFilePath Property (IInterfaceFiles)

Gets or sets where to search for DraftSight's main customization file.

## Syntax

### Visual Basic

```vb
Property CustomizationFilePath As System.String
```

### C#

```csharp
System.string CustomizationFilePath {get; set;}
```

### JScript

```
function get,set CustomizationFilePath : System.String
```

### Managed Extensions for C++

```
__property System.string* get_CustomizationFilePath();
__property void set_CustomizationFilePath(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ CustomizationFilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path where to search for DraftSight's main customization file (see **Remarks**)

## Examples

See the [IInterfaceFiles](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html) examples.

## Remarks

Use DraftSight's main customization file to add and modify user-interface elements such as menus, toolbars, and working spaces. The name of DraftSight's main customization file is **application.xml.**

## See Also

[IInterfaceFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html)
[IInterfaceFiles Members](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles_members.html)

## Availability

DraftSight V1R5.0
