---
title: "GetISO2768PartType Method (ISwDMDimXpertBlockTolerances)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertBlockTolerances"
member: "GetISO2768PartType"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances~GetISO2768PartType.html"
---

# GetISO2768PartType Method (ISwDMDimXpertBlockTolerances)

Gets the ISO 2768 part type of this DimXpert block tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetISO2768PartType( _
   ByRef type As swDmDimXpertISO2768PartType_e _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertBlockTolerances
Dim type As swDmDimXpertISO2768PartType_e
Dim value As System.Boolean

value = instance.GetISO2768PartType(type)
```

### C#

```csharp
System.bool GetISO2768PartType(
   out swDmDimXpertISO2768PartType_e type
)
```

### C++/CLI

```cpp
System.bool GetISO2768PartType(
   [Out] swDmDimXpertISO2768PartType_e type
)
```

### Parameters

- `type`: Type of ISO 2768 block tolerance as defined in [swDmDimXpertISO2768PartType_e](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.swDmDimXpertISO2768PartType_e.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertBlockTolerances::GetISO2768PartType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertBlockTolerances~GetISO2768PartType.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertBlockTolerances Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances.html)
[ISwDMDimXpertBlockTolerances Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBlockTolerances_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
