---
title: "Delete Method (IEdmLabel6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel6"
member: "Delete"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6~Delete.html"
---

# Delete Method (IEdmLabel6)

Deletes this label.

## Syntax

### Visual Basic

```vb
Sub Delete( _
   ByVal hParentWnd As System.Integer _
)
```

### C#

```csharp
void Delete(
   System.int hParentWnd
)
```

### C++/CLI

```cpp
void Delete(
   System.int hParentWnd
)
```

### Parameters

- `hParentWnd`: Parent window handle; passed to add-ins that have registered the hooks, [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).EdmCmd_PreLabelModify and EdmCmdData.EdmCmd_PostLabelModify

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmLabel6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6.html)
[IEdmLabel6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
