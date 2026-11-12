---
title: "PrintStyle Property (IRevolvedSurface)"
project: ""
interface: "IRevolvedSurface"
member: "PrintStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~PrintStyle.html"
---

# PrintStyle Property (IRevolvedSurface)

Gets or sets the name of the PrintStyle for this revolved surface.

## Syntax

### Visual Basic

```vb
ReadOnly Property PrintStyle As System.String
```

### C#

```csharp
System.string PrintStyle {get;}
```

### JScript

```
function get PrintStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PrintStyle();
```

### C++/CLI

```cpp
property System.String^ PrintStyle {
   System.String^ get();
}
```

### Property Value

Name of the PrintStyle

## Remarks

You can only set the name of a PrintStyle if named PrintStyles are used in the drawing. If color-dependent PrintStyles are used in the drawing, then the PrintStyle is set to **ByColor** and is read only. To determine the type of PrintStyle used in the document:

- call [IDocument::GetCommandOptionString](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html) and specify dsCommandOptionString_e.dsCommandOptionString_GetNmPrnStyl for the Var parameter in a project, macro, or script.
- click **Tools > Options > System Options**, expand **Printing**, expand **Default settings**, and examine **Default type** in the user-interface.

## See Also

[IRevolvedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)
[IRevolvedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface_members.html)

## Availability

DraftSight 2020 SP0
