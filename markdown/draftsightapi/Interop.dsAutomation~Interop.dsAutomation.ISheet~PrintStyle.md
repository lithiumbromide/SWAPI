---
title: "PrintStyle Property (ISheet)"
project: ""
interface: "ISheet"
member: "PrintStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~PrintStyle.html"
---

# PrintStyle Property (ISheet)

Gets or sets the name of the PrintStyle for this Sheet.

## Syntax

### Visual Basic

```vb
Property PrintStyle As System.String
```

### C#

```csharp
System.string PrintStyle {get; set;}
```

### JScript

```
function get,set PrintStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PrintStyle();
__property void set_PrintStyle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PrintStyle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the PrintStyle

## Remarks

You can only set the name of a PrintStyle if named PrintStyles are used in the drawing. If color-dependent PrintStyles are used in the drawing, then the PrintStyle is set to **ByColor** and is read only. To determine the type of PrintStyle used in the document:

- call [IDocument::GetCommandOptionString](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html) and specify dsCommandOptionString_e.dsCommandOptionString_GetNmPrnStyl for the Var parameter in a project, macro, or script.
- click **Tools > Options > System Options**, expand **Printing**, expand **Default settings**, and examine **Default type** in the user-interface.

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::PrintStyleTable Property ()](Interop.dsAutomation~Interop.dsAutomation.ISheet~PrintStyleTable.html)

## Availability

DraftSight V1R6.0
