---
title: "GetFirstParentPosition Method (IEdmReference5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmReference5"
member: "GetFirstParentPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetFirstParentPosition.html"
---

# GetFirstParentPosition Method (IEdmReference5)

Obsolete. Superseded by [IEdmReference7::GetFirstParentPosition2.](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference7~GetFirstParentPosition2.html)

## Syntax

### Visual Basic

```vb
Function GetFirstParentPosition( _
   ByVal lVersionOrZero As System.Integer, _
   ByVal bGetAllParentVersions As System.Boolean _
) As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstParentPosition(
   System.int lVersionOrZero,
   System.bool bGetAllParentVersions
)
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstParentPosition(
   System.int lVersionOrZero,
   System.bool bGetAllParentVersions
)
```

### Parameters

- `lVersionOrZero`: Non-zero value enumerates the files referencing the specified version of the file; argument is ignored if value is 0
- `bGetAllParentVersions`: True to return all versions, of all parents, referencing this file; false to return on the latest referencing version

### Return Value

[Position](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html) of first file referencing this file

## Remarks

Pass the position to [IEdmReference6::GetNextParent](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5~GetNextParent.html) to continue to enumerate all of the parent files.

C++ programmers not using smart-pointer wrapper functions must release the position.

[Return code](ReturnCodes.htm) S_OK indicates that the method successfully executed.

## See Also

[IEdmReference5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5.html)
[IEdmReference5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
