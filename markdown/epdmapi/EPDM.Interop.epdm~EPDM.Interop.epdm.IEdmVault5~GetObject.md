---
title: "GetObject Method (IEdmVault5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault5"
member: "GetObject"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html"
---

# GetObject Method (IEdmVault5)

Gets an interface to a SOLIDWORKS PDM Professional object of the specified type and having the specified ID.

## Syntax

### Visual Basic

```vb
Function GetObject( _
   ByVal eType As EdmObjectType, _
   ByVal lObjectID As System.Integer _
) As IEdmObject5
```

### C#

```csharp
IEdmObject5 GetObject(
   EdmObjectType eType,
   System.int lObjectID
)
```

### C++/CLI

```cpp
IEdmObject5^ GetObject(
   EdmObjectType eType,
   System.int lObjectID
)
```

### Parameters

- `eType`: Type of object to get as defined in [EdmObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmObjectType.html)
- `lObjectID`: ID of object to get

### Return Value

[IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html)

## Examples

[Get File References for a File (C#)](Get_File_References_for_File_Example_CSharp.htm)
[Get File References for a File (VB.NET)](Get_File_References_for_File_Example_VBNET.htm)

## Remarks

As of SOLIDWORKS PDM Professional 2008 you can call [IEdmVault9::GetObjects](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault9~GetObjects.html) to get interfaces to several objects at once, which is more efficient than calling this method multiple times.

C++ users must release the returned pointer, IEdmObject5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_ID: The provided ID was not valid.
- E_EDM_PERMISSION_DENIED: The logged-in user does not have permission to see the requested object.

## See Also

[IEdmVault5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html)
[IEdmVault5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
