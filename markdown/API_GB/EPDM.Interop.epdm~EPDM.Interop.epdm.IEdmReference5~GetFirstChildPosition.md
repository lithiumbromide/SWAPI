---
title: "GetFirstChildPosition Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "GetFirstChildPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetFirstChildPosition.html"
---

# GetFirstChildPosition Method (IEdmReference5)

Obsolete. Superseded by [IEdmReference7::GetFirstChildPosition2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstChildPosition2.html)

## Syntax

### Visual Basic

```vb
Function GetFirstChildPosition( _
   ByRef pbsProjectName As System.String, _
   ByVal bIsTopParent As System.Boolean, _
   ByVal bPermitReadLocal As System.Boolean, _
   Optional ByVal lVersion As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstChildPosition(
   out System.string pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.int lVersion
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstChildPosition(
   [Out] System.String^ pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.int lVersion
)
```

### Parameters

- `pbsProjectName`: Project name (see **Remarks**)
- `bIsTopParent`: True if this is the topmost node in the reference tree, false if not
- `bPermitReadLocal`: True to allow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database, false to disallow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database
- `lVersion`: Version for which to get references; use 0 for latest version

### Return Value

[Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of the first file referenced by this file (see **Remarks**)

## Remarks

You should maintain and pass in a string, by reference, in this argument for all calls to this method in a reference tree. The project name can be allocated and returned by the topmost node in the tree and is used by its children.

Pass the position to [IEdmReference5::GetNextChild](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html) to enumerate the referenced files.

C++ programmers not using smart-pointer wrapper functions must release the position.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)
