---
title: "GetNextRef2 Method (IEdmEnumeratorCustomReference6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnumeratorCustomReference6"
member: "GetNextRef2"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6~GetNextRef2.html"
---

# GetNextRef2 Method (IEdmEnumeratorCustomReference6)

Gets the custom file reference at the next position of an enumeration.

## Syntax

### Visual Basic

```vb
Sub GetNextRef2( _
   ByVal poPos As IEdmPos5, _
   ByRef plFileID As System.Integer, _
   ByRef plFolderID As System.Integer, _
   ByRef pbsRetPath As System.String, _
   ByRef plQuantity As System.Integer _
)
```

### C#

```csharp
void GetNextRef2(
   IEdmPos5 poPos,
   out System.int plFileID,
   out System.int plFolderID,
   out System.string pbsRetPath,
   out System.int plQuantity
)
```

### C++/CLI

```cpp
void GetNextRef2(
   IEdmPos5^ poPos,
   [Out] System.int plFileID,
   [Out] System.int plFolderID,
   [Out] System.String^ pbsRetPath,
   [Out] System.int plQuantity
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next custom file reference
- `plFileID`: ID of the referenced file
- `plFolderID`: ID of the parent folder of the referenced file
- `pbsRetPath`: Path name of the referenced file
- `plQuantity`: Number of times the referenced file is referenced

## Examples

See the [IEdmEnumeratorCustomReference6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6.html) examples.

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first custom file reference, IEdmPos5. Call [IEdmEnumeratorCustomReference5::GetFirstRefPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference5~GetFirstRefPosition.html) to obtain IEdmPos5.

After this method is called the first time, poPos is automatically incremented every time it is called.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmEnumeratorCustomReference6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6.html)
[IEdmEnumeratorCustomReference6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorCustomReference6_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
