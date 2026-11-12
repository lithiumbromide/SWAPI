---
title: "GetDrawingPropSheetAttributes Method (IEdmVariableMgr7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr7"
member: "GetDrawingPropSheetAttributes"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr7~GetDrawingPropSheetAttributes.html"
---

# GetDrawingPropSheetAttributes Method (IEdmVariableMgr7)

Gets all of the SLDDRW-card attributes that are linked to the $PRPSHEET block for the specified folder.

## Syntax

### Visual Basic

```vb
Sub GetDrawingPropSheetAttributes( _
   ByVal lFolderID As System.Integer, _
   ByRef ppoSrcAttribs() As System.String, _
   ByRef ppoDestAttribs() As System.String _
)
```

### C#

```csharp
void GetDrawingPropSheetAttributes(
   System.int lFolderID,
   out System.string[] ppoSrcAttribs,
   out System.string[] ppoDestAttribs
)
```

### C++/CLI

```cpp
void GetDrawingPropSheetAttributes(
   System.int lFolderID,
   [Out] System.array<String^>^ ppoSrcAttribs,
   [Out] System.array<String^>^ ppoDestAttribs
)
```

### Parameters

- `lFolderID`: ID of folder from which to get the values
- `ppoSrcAttribs`: Array of attribute names used in the CustomProperty block
- `ppoDestAttribs`: Array of attribute names used in the $PRPSheet block

## Remarks

This method is used internally by SOLIDWORKS PDM Professional to copy attributes from the model's CustomProperty block to the $PRPSHEET block. ppoSrcAttribs and ppoDestAttribs both have the same number of elements.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableMgr7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr7.html)
[IEdmVariableMgr7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr7_members.html)

## Availability

SOLIDWORKS PDM Professional 2011
