---
title: "Language Property (IMacroManager)"
project: ""
interface: "IMacroManager"
member: "Language"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMacroManager~Language.html"
---

# Language Property (IMacroManager)

Gets or sets the language in which to record the [macro](Macros.htm).

## Syntax

### Visual Basic

```vb
Property Language As dsMacroLanguage_e
```

### C#

```csharp
dsMacroLanguage_e Language {get; set;}
```

### JScript

```
function get,set Language : dsMacroLanguage_e
```

### Managed Extensions for C++

```
__property dsMacroLanguage_e get_Language();
__property void set_Language(
   dsMacroLanguage_e value
);
```

### C++/CLI

```cpp
property dsMacroLanguage_e Language {
   dsMacroLanguage_e get();
   void set (    dsMacroLanguage_e value);
}
```

### Property Value

Language in which to record the macro as defined in [dsMacroLanguage_e](Interop.dsAutomation~Interop.dsAutomation.dsMacroLanguage_e.html)

## Examples

See the [IMacroManager](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html) examples.

## See Also

[IMacroManager Interface](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html)
[IMacroManager Members](Interop.dsAutomation~Interop.dsAutomation.IMacroManager_members.html)
[IMacroManager::StartMacroRecording Method ()](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StartMacroRecording.html)

## Availability

DraftSight V1R5.0
