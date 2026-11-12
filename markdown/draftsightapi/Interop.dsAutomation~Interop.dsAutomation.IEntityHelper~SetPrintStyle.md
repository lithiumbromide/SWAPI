---
title: "SetPrintStyle Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "SetPrintStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~SetPrintStyle.html"
---

# SetPrintStyle Method (IEntityHelper)

Sets the name of the PrintStyle for the specified entity.

## Syntax

### Visual Basic

```vb
Sub SetPrintStyle( _
   ByVal Obj As System.Object, _
   ByVal Val As System.String _
)
```

### C#

```csharp
void SetPrintStyle(
   System.object Obj,
   System.string Val
)
```

### JScript

```
function SetPrintStyle(
   Obj : System.Object,
   Val : System.String
);
```

### Managed Extensions for C++

```
void SetPrintStyle(
   System.Object* Obj,
   System.string* Val
)
```

### C++/CLI

```cpp
void SetPrintStyle(
   System.Object^ Obj,
   System.String^ Val
)
```

### Parameters

- `Obj`: Entity for which to set the name of the PrintStyle
- `Val`: Name of the PrintStyle

## Remarks

You can only set the name of a PrintStyle if named PrintStyles are used in the drawing. If color-dependent PrintStyles are used in the drawing, then the PrintStyle is set to **ByColor** and is read only. To determine the type of PrintStyle used in the document:

- call [IDocument::GetCommandOptionString](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html) and specify dsCommandOptionString_e.dsCommandOptionString_GetNmPrnStyl for the Var parameter in a project, macro, or script.
- click **Tools > Options > System Options**, expand **Printing**, expand **Default** **settings**, and examine **Default type** in the user-interface.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetPrintStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetPrintStyle.html)

## Availability

DraftSight V1R6.0
