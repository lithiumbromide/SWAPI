---
title: "SetSetupPages Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "SetSetupPages"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSetupPages.html"
---

# SetSetupPages Method (IEdmTaskProperties)

Adds setup pages to the task property dialog box for this task definition.

## Syntax

### Visual Basic

```vb
Sub SetSetupPages( _
   ByVal poPages() As EdmTaskSetupPage _
)
```

### C#

```csharp
void SetSetupPages(
   EdmTaskSetupPage[] poPages
)
```

### C++/CLI

```cpp
void SetSetupPages(
   array<EdmTaskSetupPage>^ poPages
)
```

### Parameters

- `poPages`: Array of [EdmTaskSetupPage](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage.html) structures; one structure for each setup page

## Examples

[Create a Task that Finds Files in Workflow States (VB.NET)](Schedule_Task_to_Find_Files_in_State_Addin_Example_VBNET.htm)
[Create a Task that Finds Files in Workflow States (C#)](Schedule_Task_to_Find_Files_in_State_Addin_Example_CSharp.htm)

## Remarks

Call this method during the processing of the [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_TaskSetup hook. The setup pages display when the task is double-clicked in the administration tool.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
