---
title: "PaperSpaceSelectionEnabled Property (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "PaperSpaceSelectionEnabled"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~PaperSpaceSelectionEnabled.html"
---

# PaperSpaceSelectionEnabled Property (ISelectionManager)

Gets or sets whether paper-space selection is enabled.

## Syntax

### Visual Basic

```vb
Property PaperSpaceSelectionEnabled As System.Boolean
```

### C#

```csharp
System.bool PaperSpaceSelectionEnabled {get; set;}
```

### JScript

```
function get,set PaperSpaceSelectionEnabled : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_PaperSpaceSelectionEnabled();
__property void set_PaperSpaceSelectionEnabled(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool PaperSpaceSelectionEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to enable paper-space selection, false to disable it

## Remarks

This property affects these single-selection methods only:

- [ICommandMessage::PromptForSelection](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelection.html) and [ICommandMessage::PromptForSelectionOrKeyword](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForSelectionOrKeyword.html) with the SingleSelect parameter set to true
- [ISelectionManager::SelectByPoint](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPoint.html)

When paper-space selection is enabled, then these methods can select entities from model space. These methods can also select entities when the active sheet is not the model sheet and paper-space selection is enabled.

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)

## Availability

DraftSight V1R5
