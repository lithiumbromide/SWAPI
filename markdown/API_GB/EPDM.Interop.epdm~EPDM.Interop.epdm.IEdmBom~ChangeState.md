---
title: "ChangeState Method (IEdmBom)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBom"
member: "ChangeState"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom~ChangeState.html"
---

# ChangeState Method (IEdmBom)

Changes the workflow state of this BOM.

## Syntax

### Visual Basic

```vb
Sub ChangeState( _
   ByVal poStateIdOrName As System.Object, _
   ByVal bsComment As System.String, _
   ByVal lParentWnd As System.Integer, _
   Optional ByVal lEdmStateFlags As System.Integer _
)
```

### C#

```csharp
void ChangeState(
   System.object poStateIdOrName,
   System.string bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags
)
```

### C++/CLI

```cpp
void ChangeState(
   System.Object^ poStateIdOrName,
   System.String^ bsComment,
   System.int lParentWnd,
   System.int lEdmStateFlags
)
```

### Parameters

- `poStateIdOrName`: Name or ID of new workflow state
- `bsComment`: Comment to append to the history of this BOM
- `lParentWnd`: Parent window handle; passed to registered add-ins
- `lEdmStateFlags`: Combination of [EdmStateFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmStateFlags.html) bits

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBom Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom.html)
[IEdmBom Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBom_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
