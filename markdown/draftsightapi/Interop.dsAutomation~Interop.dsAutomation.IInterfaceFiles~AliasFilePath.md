---
title: "AliasFilePath Property (IInterfaceFiles)"
project: ""
interface: "IInterfaceFiles"
member: "AliasFilePath"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles~AliasFilePath.html"
---

# AliasFilePath Property (IInterfaceFiles)

Gets or sets where to search for the alias commands file.

## Syntax

### Visual Basic

```vb
Property AliasFilePath As System.String
```

### C#

```csharp
System.string AliasFilePath {get; set;}
```

### JScript

```
function get,set AliasFilePath : System.String
```

### Managed Extensions for C++

```
__property System.string* get_AliasFilePath();
__property void set_AliasFilePath(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ AliasFilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path where to search for the alias commands file

## Examples

See the [IInterfaceFiles](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html) examples.

## Remarks

The file name of the alias commands file is **alias.xml**.

## See Also

[IInterfaceFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html)
[IInterfaceFiles Members](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles_members.html)

## Availability

DraftSight V1R5.0
