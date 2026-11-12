---
title: "GetEndFeatures Method (ISwDMDimXpertCompoundClosedSlot3dFeature)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDimXpertCompoundClosedSlot3dFeature"
member: "GetEndFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.html"
---

# GetEndFeatures Method (ISwDMDimXpertCompoundClosedSlot3dFeature)

Gets the DimXpert features at both closed ends of this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndFeatures( _
   ByRef End1 As SwDMDimXpertFeature, _
   ByRef End2 As SwDMDimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDimXpertCompoundClosedSlot3dFeature
Dim End1 As SwDMDimXpertFeature
Dim End2 As SwDMDimXpertFeature
Dim value As System.Boolean

value = instance.GetEndFeatures(End1, End2)
```

### C#

```csharp
System.bool GetEndFeatures(
   out SwDMDimXpertFeature End1,
   out SwDMDimXpertFeature End2
)
```

### C++/CLI

```cpp
System.bool GetEndFeatures(
   [Out] SwDMDimXpertFeature^ End1,
   [Out] SwDMDimXpertFeature^ End2
)
```

### Parameters

- `End1`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)
- `End2`: [ISwDMDimXpertFeature](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDimXpertFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [SwDMDimXpertCompoundClosedSlot3dFeature::GetEndFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.html).

## Examples

See the examples on the interface page.

## See Also

[ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.html)
[ISwDMDimXpertCompoundClosedSlot3dFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
