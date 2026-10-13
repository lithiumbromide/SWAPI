---
title: "GetParallelTransitionInfo Method (IEdmTransition9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition9"
member: "GetParallelTransitionInfo"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9~GetParallelTransitionInfo.html"
---

# GetParallelTransitionInfo Method (IEdmTransition9)

Gets the required information for the parallel transition of the specified document and project.

## Syntax

### Visual Basic

```vb
Sub GetParallelTransitionInfo( _
   ByVal lDocumentID As System.Integer, _
   ByVal lProjectID As System.Integer, _
   ByRef plReqNum As System.Integer, _
   ByRef plCommitNum As System.Integer, _
   ByRef pbRevoke As System.Boolean _
)
```

### C#

```csharp
void GetParallelTransitionInfo(
   System.int lDocumentID,
   System.int lProjectID,
   out System.int plReqNum,
   out System.int plCommitNum,
   out System.bool pbRevoke
)
```

### C++/CLI

```cpp
void GetParallelTransitionInfo(
   System.int lDocumentID,
   System.int lProjectID,
   [Out] System.int plReqNum,
   [Out] System.int plCommitNum,
   [Out] System.bool pbRevoke
)
```

### Parameters

- `lDocumentID`: Document ID
- `lProjectID`: Project ID
- `plReqNum`: Number of this parallel transition
- `plCommitNum`: Number of committed users
- `pbRevoke`: True to revoke, false to not

## See Also

[IEdmTransition9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9.html)
[IEdmTransition9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition9_members.html)
