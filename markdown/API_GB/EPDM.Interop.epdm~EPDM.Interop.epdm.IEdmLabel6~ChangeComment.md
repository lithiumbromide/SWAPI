---
title: "ChangeComment Method (IEdmLabel6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmLabel6"
member: "ChangeComment"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmLabel6~ChangeComment.html"
---

# ChangeComment Method (IEdmLabel6)

Updates the comment of this label.

## Syntax

### Visual Basic

```vb
Sub ChangeComment( _
   ByVal bsComment As System.String, _
   ByVal hParentWnd As System.Integer _
)
```

### C#

```csharp
void ChangeComment(
   System.string bsComment,
   System.int hParentWnd
)
```

### C++/CLI

```cpp
void ChangeComment(
   System.String^ bsComment,
   System.int hParentWnd
)
```

### Parameters

- `bsComment`: New comment for this label
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
