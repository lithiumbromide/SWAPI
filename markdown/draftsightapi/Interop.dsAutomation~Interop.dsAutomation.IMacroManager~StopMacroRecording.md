---
title: "StopMacroRecording Method (IMacroManager)"
project: ""
interface: "IMacroManager"
member: "StopMacroRecording"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StopMacroRecording.html"
---

# StopMacroRecording Method (IMacroManager)

Stops [macro recording](Macros.htm) and saves the macro to the specified folder and file names.

## Syntax

### Visual Basic

```vb
Sub StopMacroRecording( _
   ByVal MacroName As System.String _
)
```

### C#

```csharp
void StopMacroRecording(
   System.string MacroName
)
```

### JScript

```
function StopMacroRecording(
   MacroName : System.String
);
```

### Managed Extensions for C++

```
void StopMacroRecording(
   System.string* MacroName
)
```

### C++/CLI

```cpp
void StopMacroRecording(
   System.String^ MacroName
)
```

### Parameters

- `MacroName`: Name of folder where to save the macro and the name of the Visual Studio 2008 project files or the name of the **.swb** file to which to save the macro

## Examples

See the [IMacroManager](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html) examples.

## See Also

[IMacroManager Interface](Interop.dsAutomation~Interop.dsAutomation.IMacroManager.html)
[IMacroManager Members](Interop.dsAutomation~Interop.dsAutomation.IMacroManager_members.html)
[IMacroManager::SavePath Property ()](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~SavePath.html)
[IMacroManager::StartMacroRecording Method ()](Interop.dsAutomation~Interop.dsAutomation.IMacroManager~StartMacroRecording.html)

## Availability

DraftSight V1R5.0
