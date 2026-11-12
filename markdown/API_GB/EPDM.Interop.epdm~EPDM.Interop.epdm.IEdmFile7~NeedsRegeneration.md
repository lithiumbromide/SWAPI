---
title: "NeedsRegeneration Method (IEdmFile7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile7"
member: "NeedsRegeneration"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~NeedsRegeneration.html"
---

# NeedsRegeneration Method (IEdmFile7)

Gets whether the file with the specified version and location needs to be rebuilt in its associated CAD program.

## Syntax

### Visual Basic

```vb
Function NeedsRegeneration( _
   ByVal lVersion As System.Integer, _
   Optional ByVal oFolderPathOrID As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool NeedsRegeneration(
   System.int lVersion,
   System.object oFolderPathOrID
)
```

### C++/CLI

```cpp
System.bool NeedsRegeneration(
   System.int lVersion,
   System.Object^ oFolderPathOrID
)
```

### Parameters

- `lVersion`: File version; 0 to check the version in the local cache
- `oFolderPathOrID`: Path or ID of the file's parent folder; valid only if lVersion is not 0

### Return Value

True if the file needs to be rebuilt in its associated CAD program, false if not

## Remarks

If you have a drawing that references a part, and you make a model change on the part and don't rebuild the drawing in the CAD program, then the drawing shows the earlier version of the part. Use this method to check whether the drawing needs to be rebuilt with the newer version of the part in the associated CAD program.

Support for rebuild checks is only available for files saved with SOLIDWORKS 2009 or later.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html)
[IEdmFile7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
