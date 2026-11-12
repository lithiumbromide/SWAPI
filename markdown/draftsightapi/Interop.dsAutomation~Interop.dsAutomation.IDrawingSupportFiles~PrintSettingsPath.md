---
title: "PrintSettingsPath Property (IDrawingSupportFiles)"
project: ""
interface: "IDrawingSupportFiles"
member: "PrintSettingsPath"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles~PrintSettingsPath.html"
---

# PrintSettingsPath Property (IDrawingSupportFiles)

Gets or sets the path for print configurations.

## Syntax

### Visual Basic

```vb
Property PrintSettingsPath As System.String
```

### C#

```csharp
System.string PrintSettingsPath {get; set;}
```

### JScript

```
function get,set PrintSettingsPath : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PrintSettingsPath();
__property void set_PrintSettingsPath(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PrintSettingsPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Path for print configurations

## Remarks

Print configurations are stored in files with a **.cfg** filename extension.

## See Also

[IDrawingSupportFiles Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles.html)
[IDrawingSupportFiles Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingSupportFiles_members.html)
[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)

## Availability

DraftSight V1R5.0
