---
title: "LevelOfDetail Property (IMacroManager)"
project: ""
interface: "IMacroManager"
member: "LevelOfDetail"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMacroManager~LevelOfDetail.html"
---

# LevelOfDetail Property (IMacroManager)

Gets or sets the level of detail in which to record the [macro](Macros.htm).

## Syntax

### Visual Basic

```vb
Property LevelOfDetail As dsMacroLevelOfDetail_e
```

### C#

```csharp
dsMacroLevelOfDetail_e LevelOfDetail {get; set;}
```

### JScript

```
function get,set LevelOfDetail : dsMacroLevelOfDetail_e
```

### Managed Extensions for C++

```
__property dsMacroLevelOfDetail_e get_LevelOfDetail();
__property void set_LevelOfDetail(
   dsMacroLevelOfDetail_e value
);
```

### C++/CLI

```cpp
property dsMacroLevelOfDetail_e LevelOfDetail {
   dsMacroLevelOfDetail_e get();
   void set (    dsMacroLevelOfDetail_e value);
}
```

### Property Value

Level of detail in which to record the macro as defined in [dsMacroLevelOfDetail_e](Interop.dsAutomation~Interop.dsAutomation.dsMacroLevelOfDetail_e.html)

## Examples

See the [IMacroManager](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html) examples.

## See Also

[IMacroManager Interface](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html)
[IMacroManager Members](Interop.dsAutomation~Interop.dsAutomation.IMacroManager_members.html)
[IMacroManager::StartMacroRecording Method ()](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StartMacroRecording.html)

## Availability

DraftSight V1R5.0
