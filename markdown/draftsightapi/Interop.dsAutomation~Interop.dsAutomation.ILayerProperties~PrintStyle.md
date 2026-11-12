---
title: "PrintStyle Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "PrintStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~PrintStyle.html"
---

# PrintStyle Property (ILayerProperties)

Gets or sets the PrintStyle for this Layer.

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

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

You can only set the name of a PrintStyle if named PrintStyles are used in the drawing. If color-dependent PrintStyles are used in the drawing, then the PrintStyle is set to **ByColor** and is read only. To determine the type of PrintStyle used in the document:

- Call [IDocument::GetCommandOptionString](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html) and specify dsCommandOptionString_e.dsCommandOptionString_GetNmPrnStyl for the Var parameter in a project, macro, or script.
- Click **Tools > Options > System OptionsPrinting**, expand **Printing**, expand **Default settings**, and examine **Default type** in the user-interface.

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
