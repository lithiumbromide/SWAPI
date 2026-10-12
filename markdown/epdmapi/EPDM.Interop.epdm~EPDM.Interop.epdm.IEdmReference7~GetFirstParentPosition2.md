---
title: "GetFirstParentPosition2 Method (IEdmReference7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference7"
member: "GetFirstParentPosition2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstParentPosition2.html"
---

# GetFirstParentPosition2 Method (IEdmReference7)

Starts an enumeration of parent references.

## Syntax

### Visual Basic

```vb
Function GetFirstParentPosition2( _
   ByVal lVersionOrZero As System.Integer, _
   ByVal bGetAllParentVersions As System.Boolean, _
   ByVal lEdmRefFlags As System.Integer _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstParentPosition2(
   System.int lVersionOrZero,
   System.bool bGetAllParentVersions,
   System.int lEdmRefFlags
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstParentPosition2(
   System.int lVersionOrZero,
   System.bool bGetAllParentVersions,
   System.int lEdmRefFlags
)
```

### Parameters

- `lVersionOrZero`: Non-0 value enumerates the files referencing the specified version of the file; argument is ignored if value is 0
- `bGetAllParentVersions`: True to return all versions, of all parents, referencing this file; false to return on the latest referencing version
- `lEdmRefFlags`: Types of references that you want enumerated as defined in [EdmRefFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRefFlags.html)

### Return Value

[Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of first file referencing this file

## Examples

See the [IEdmReference7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html) examples.

## Remarks

Pass the position to [IEdmReference5::GetNextParent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextParent.html) to continue to enumerate all of the parent files.

C++ programmers not using smart-pointer wrapper functions must release the position.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7.html)
[IEdmReference7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
