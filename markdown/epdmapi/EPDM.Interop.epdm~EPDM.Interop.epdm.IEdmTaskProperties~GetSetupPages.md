---
title: "GetSetupPages Method (IEdmTaskProperties)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTaskProperties"
member: "GetSetupPages"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~GetSetupPages.html"
---

# GetSetupPages Method (IEdmTaskProperties)

Gets the setup pages added to the task property dialog box using [IEdmTaskProperties::SetSetupPages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties~SetSetupPages.html).

## Syntax

### Visual Basic

```vb
Sub GetSetupPages( _
   ByRef ppoPages() As EdmTaskSetupPage _
)
```

### C#

```csharp
void GetSetupPages(
   out EdmTaskSetupPage[] ppoPages
)
```

### C++/CLI

```cpp
void GetSetupPages(
   [Out] array<EdmTaskSetupPage>^ ppoPages
)
```

### Parameters

- `ppoPages`: Array of [EdmTaskSetupPage](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmTaskSetupPage.html) structures; one structure for each setup page

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTaskProperties Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties.html)
[IEdmTaskProperties Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTaskProperties_members.html)
[Task Add-in Sample](TaskSample.htm)

## Availability

SOLIDWORKS PDM Professional 2010
