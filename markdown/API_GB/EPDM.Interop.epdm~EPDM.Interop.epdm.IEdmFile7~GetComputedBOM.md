---
title: "GetComputedBOM Method (IEdmFile7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile7"
member: "GetComputedBOM"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7~GetComputedBOM.html"
---

# GetComputedBOM Method (IEdmFile7)

Gets an interface to a computed Bill of Materials.

## Syntax

### Visual Basic

```vb
Function GetComputedBOM( _
   ByVal oBomLayoutNameOrID As System.Object, _
   ByVal lVersionNo As System.Integer, _
   ByVal bsConfiguration As System.String, _
   ByVal lEdmBomFlags As System.Integer _
) As EdmBomView
```

### C#

```csharp
EdmBomView GetComputedBOM(
   System.object oBomLayoutNameOrID,
   System.int lVersionNo,
   System.string bsConfiguration,
   System.int lEdmBomFlags
)
```

### C++/CLI

```cpp
EdmBomView^ GetComputedBOM(
   System.Object^ oBomLayoutNameOrID,
   System.int lVersionNo,
   System.String^ bsConfiguration,
   System.int lEdmBomFlags
)
```

### Parameters

- `oBomLayoutNameOrID`: Name or ID of a Bill of Materials layout (see **Remarks**)
- `lVersionNo`: Version of file for which to get the Bill of Materials; 0 or -1 to use the latest version
- `bsConfiguration`: Name of the file configuration
- `lEdmBomFlags`: Combination of [EdmBomFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomFlag.html) bits

### Return Value

[IEdmBomView](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView.html)

## Examples

See the [IEdmFile7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html) examples.

## Remarks

To specify oBomLayoutNameOrID, use [IEdmBomMgr.GetBomLayouts](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr~GetBomLayouts.html) to enumerate the existing Bill of Materials layouts.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFile7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7.html)
[IEdmFile7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile7_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
