---
title: "GetFirstChildPosition4 Method (IEdmReference10)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference10"
member: "GetFirstChildPosition4"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference10~GetFirstChildPosition4.html"
---

# GetFirstChildPosition4 Method (IEdmReference10)

Starts an enumeration of child references for the specified configuration.

## Syntax

### Visual Basic

```vb
Function GetFirstChildPosition4( _
   ByRef pbsProjectName As System.String, _
   ByVal bIsTopParent As System.Boolean, _
   ByVal bPermitReadLocal As System.Boolean, _
   ByVal bGetSuppressedComponent As System.Boolean, _
   ByVal lEdmRefFlags As System.Integer, _
   ByVal bsConfiguration As System.String, _
   Optional ByVal lVersion As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstChildPosition4(
   out System.string pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.bool bGetSuppressedComponent,
   System.int lEdmRefFlags,
   System.string bsConfiguration,
   System.int lVersion
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstChildPosition4(
   [Out] System.String^ pbsProjectName,
   System.bool bIsTopParent,
   System.bool bPermitReadLocal,
   System.bool bGetSuppressedComponent,
   System.int lEdmRefFlags,
   System.String^ bsConfiguration,
   System.int lVersion
)
```

### Parameters

- `pbsProjectName`: Project name (see **Remarks**)
- `bIsTopParent`: True if this is the topmost node in the reference tree, false if not
- `bPermitReadLocal`: True to allow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database, false to disallow SOLIDWORKS PDM Professional to read reference information if it is not already present in the database
- `bGetSuppressedComponent`: True to get a suppressed reference, false to not
- `lEdmRefFlags`: Types of references that you want enumerated as defined in [EdmRefFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefFlags.html)
- `bsConfiguration`: Configuration name for which to get child references (see **Remarks**)
- `lVersion`: Version for which to get references; use 0 for latest version

### Return Value

[Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of the first file referenced by this file (see **Remarks**)

## Examples

[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)
[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)

## Remarks

You should maintain and pass in a string, by reference, in this argument for all calls to this method in a reference tree. The project name can be allocated and returned by the topmost node in the tree and is used by its children.

[IEdmReference6::RefCount](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference6~RefCount.html) and [IEdmReference8::RefCountEdited](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference8~RefCountEdited.html) for child references return values for corresponding referenced configurations. If an empty string is passed to bsConfiguration, then the file's common configuration is used.

Pass the position returned by this method to [IEdmReference5::GetNextChild](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextChild.html) to continue to enumerate the referenced files.

C++ programmers not using smart-pointer wrapper functions must release the position.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference10 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference10.html)
[IEdmReference10 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference10_members.html)

## Availability

SOLIDWORKS PDM Professional 2015
