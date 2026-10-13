---
title: "AddInternalComponent Method (IEdmBatchListing3)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchListing3"
member: "AddInternalComponent"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3~AddInternalComponent.html"
---

# AddInternalComponent Method (IEdmBatchListing3)

Adds the specified internal component to the batch for listing.

## Syntax

### Visual Basic

```vb
Sub AddInternalComponent( _
   ByVal oPath As System.Object, _
   ByVal oID As System.Object, _
   ByVal oVirtualFileParentPath As System.Object, _
   ByVal oFileDate As System.Date, _
   ByVal lParam As System.Integer, _
   Optional ByVal bsConfigName As System.String, _
   Optional ByVal lEdmListFileFlags As System.Integer _
)
```

### C#

```csharp
void AddInternalComponent(
   System.object oPath,
   System.object oID,
   System.object oVirtualFileParentPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.string bsConfigName,
   System.int lEdmListFileFlags
)
```

### C++/CLI

```cpp
void AddInternalComponent(
   System.Object^ oPath,
   System.Object^ oID,
   System.Object^ oVirtualFileParentPath,
   System.DateTime oFileDate,
   System.int lParam,
   System.String^ bsConfigName,
   System.int lEdmListFileFlags
)
```

### Parameters

- `oPath`: Path of internal component
- `oID`: ID of internal component
- `oVirtualFileParentPath`: Path of parent folder
- `oFileDate`: Date of file
- `lParam`: User-defined argument
- `bsConfigName`: Name of the configuration file from which to read variables
- `lEdmListFileFlags`: Combination of [EdmListFileFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmListFileFlags.html) bits

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchListing3 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3.html)
[IEdmBatchListing3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchListing3_members.html)

## Availability

SOLIDWORKS PDM Professional 2010
