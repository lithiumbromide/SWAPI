---
title: "GetRevisionNumberIDFromFile Method (IEdmRevisionMgr2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRevisionMgr2"
member: "GetRevisionNumberIDFromFile"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2~GetRevisionNumberIDFromFile.html"
---

# GetRevisionNumberIDFromFile Method (IEdmRevisionMgr2)

Gets the active revision number of the specified file.

## Syntax

### Visual Basic

```vb
Function GetRevisionNumberIDFromFile( _
   ByVal lFileID As System.Integer, _
   ByRef pbCanIncrement As System.Boolean _
) As System.Integer
```

### C#

```csharp
System.int GetRevisionNumberIDFromFile(
   System.int lFileID,
   out System.bool pbCanIncrement
)
```

### C++/CLI

```cpp
System.int GetRevisionNumberIDFromFile(
   System.int lFileID,
   [Out] System.bool pbCanIncrement
)
```

### Parameters

- `lFileID`: ID of file for which to get a revision number (see **Remarks**)
- `pbCanIncrement`: True if the next increment will succeed, false if not

### Return Value

Revision number ID; 0 if no revision number is found for the file

## Examples

[Set Initial Revision (VB.NET)](Set_Initial_Revision_Example_VBNET.htm)
[Set Initial Revision (C#)](Set_Initial_Revision_Example_CSharp.htm)

## Remarks

Before calling this method, set lFileID using [IEdmFile5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html).ID.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmRevisionMgr2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2.html)
[IEdmRevisionMgr2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRevisionMgr2_members.html)

## Availability

SOLIDWORKS PDM Professional 2007 SP03
