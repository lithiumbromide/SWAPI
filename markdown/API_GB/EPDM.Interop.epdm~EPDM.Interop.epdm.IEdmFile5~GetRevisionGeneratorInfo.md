---
title: "GetRevisionGeneratorInfo Method (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "GetRevisionGeneratorInfo"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~GetRevisionGeneratorInfo.html"
---

# GetRevisionGeneratorInfo Method (IEdmFile5)

Gets information about this file for the revision generator.

## Syntax

### Visual Basic

```vb
Function GetRevisionGeneratorInfo( _
   ByRef pbIncrementMenu As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool GetRevisionGeneratorInfo(
   out System.bool pbIncrementMenu
)
```

### C++/CLI

```cpp
System.bool GetRevisionGeneratorInfo(
   [Out] System.bool pbIncrementMenu
)
```

### Parameters

- `pbIncrementMenu`: True if there should be an Increment Revision menu item in the context menu of this file, false if not

### Return Value

True if there is a revision number generator set up for the file's current state in the workflow, false if not

## Remarks

This method exists mainly for internal purposes.

See [Return Codes](ReturnCodes.htm) for the complete list of potential success and error codes. The following are just a few examples:

- S_OK: The method successfully executed.
- E_EDM_END_OF_REV_GEN_LIST_STOP: It is not possible to increment revision on this file, because SOLIDWORKS PDM Professional has reached the end of the revision list that was set up in the Workflow Editor.

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
