---
title: "RemoveOptions Property (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "RemoveOptions"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~RemoveOptions.html"
---

# RemoveOptions Property (ISelectionManager)

Gets or sets whether to allow or disallow the selection of an entity.

## Syntax

### Visual Basic

```vb
Property RemoveOptions As System.Integer
```

### C#

```csharp
System.int RemoveOptions {get; set;}
```

### JScript

```
function get,set RemoveOptions : System.int
```

### Managed Extensions for C++

```
__property System.int get_RemoveOptions();
__property void set_RemoveOptions(
   System.int value
);
```

### C++/CLI

```cpp
property System.int RemoveOptions {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Allow or disallow the selection of the entity as defined in [dsSelectionRemove_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionRemove_e.html)

## Remarks

You can use this method to select an entity whose selection is typically disallowed in DraftSight; e.g., selecting an entity on a locked Layer in order to dimension that entity.

Use this method in combination with such methods as [ICommandMessage::PromptForSelection](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelection.html) and [ICommandMessage::PromptForSelectionOrKeyword](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelectionOrKeyword.html) to allow and disallow selection of entities.

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)

## Availability

DraftSight V1R5.1
