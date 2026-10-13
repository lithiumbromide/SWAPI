---
title: "VerUpgrade_ReferenceCheck Method (IEdmRevisionMgr3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr3"
member: "VerUpgrade_ReferenceCheck"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3~VerUpgrade_ReferenceCheck.html"
---

# VerUpgrade_ReferenceCheck Method (IEdmRevisionMgr3)

Finds parts that are referenced by assemblies and where the referenced part version is not the latest version.

## Syntax

### Visual Basic

```vb
Sub VerUpgrade_ReferenceCheck( _
   ByVal poFiles() As EdmSelItem, _
   ByRef ppoWrongRefs() As EdmCheckRef _
)
```

### C#

```csharp
void VerUpgrade_ReferenceCheck(
   EdmSelItem[] poFiles,
   out EdmCheckRef[] ppoWrongRefs
)
```

### C++/CLI

```cpp
void VerUpgrade_ReferenceCheck(
   array<EdmSelItem>^ poFiles,
   [Out] array<EdmCheckRef>^ ppoWrongRefs
)
```

### Parameters

- `poFiles`: Array of [EdmSelItem](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSelItem.html) structures; one structure for each assembly file for which to find references
- `ppoWrongRefs`: Array of [EdmCheckRef](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCheckRef.html) structures; one structure for each part that is referenced in an earlier version than the lastest version

## Remarks

You need to be logged in as a user that has permission to update revision numbers ([EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html).EdmSysRight_ModifyRevisionNumbers) in order to use this method. The reason you need this high level of permission is that this method overrides read permission on the files and returns files that the logged-in user lacks permission to see.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3.html)
[IEdmRevisionMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr3_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
