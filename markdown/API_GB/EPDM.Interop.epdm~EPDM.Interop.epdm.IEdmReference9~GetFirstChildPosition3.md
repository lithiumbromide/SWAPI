---
title: "GetFirstChildPosition3 Method (IEdmReference9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference9"
member: "GetFirstChildPosition3"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9~GetFirstChildPosition3.html"
---

# GetFirstChildPosition3 Method (IEdmReference9)

Obsolete. Superseded by [IEdmReference10::GetFirstChildPosition4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference10~GetFirstChildPosition4.html).

## Syntax

### Visual Basic

```vb
Function GetFirstChildPosition3( _
   ByRef pbsProjectName As System.String, _
   ByVal bIsTopParent As System.Boolean, _
   ByVal bPermitReadLocal As System.Boolean, _
   ByVal lEdmRefFlags As System.Integer, _
   ByVal bsConfiguration As System.String, _
   Optional ByVal lVersion As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstChildPosition3(
   out System.string pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.int lEdmRefFlags,
   System.string bsConfiguration,
   System.int lVersion
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstChildPosition3(
   [Out] System.String^ pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.int lEdmRefFlags,
   System.String^ bsConfiguration,
   System.int lVersion
)
```

### Parameters

- `pbsProjectName`: Project name (see **Remarks**)
- `bIsTopParent`: True if this is the topmost node in the reference tree, false if not
- `bPermitReadLocal`: True to allow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database, false to disallow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database
- `lEdmRefFlags`: Types of references that you want enumerated as defined in [EdmRefFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefFlags.html)
- `bsConfiguration`: Configuration name for which to get child references (see **Remarks**)
- `lVersion`: Version for which to get references; use 0 for latest version

### Return Value

[Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of the first file referenced by this file (see **Remarks**)

## Remarks

You should maintain and pass in a string, by reference, in this argument for all calls to this method in a reference tree. The project name can be allocated and returned by the topmost node in the tree and is used by its children.

[IEdmReference6::RefCount](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6~RefCount.html) and [IEdmReference8::RefCountEdited](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8~RefCountEdited.html) for child references return values for corresponding referenced configurations. If an empty string is passed to bsConfiguration, then the file's common configuration is used.

Pass the position returned by this method to [IEdmReference5::GetNextChild](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html) to continue to enumerate the referenced files.

C++ programmers not using smart-pointer wrapper functions must release the position.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9.html)
[IEdmReference9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference9_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
