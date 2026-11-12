---
title: "HasFrozenFeatures Method (ISwDMDocument16)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument16"
member: "HasFrozenFeatures"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16~HasFrozenFeatures.html"
---

# HasFrozenFeatures Method (ISwDMDocument16)

Gets whether the document has frozen features and whether those features need to be updated.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasFrozenFeatures( _
   ByRef FrozenFeatureNeedsUpdate As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument16
Dim FrozenFeatureNeedsUpdate As System.Boolean
Dim value As System.Boolean

value = instance.HasFrozenFeatures(FrozenFeatureNeedsUpdate)
```

### C#

```csharp
System.bool HasFrozenFeatures(
   out System.bool FrozenFeatureNeedsUpdate
)
```

### C++/CLI

```cpp
System.bool HasFrozenFeatures(
   [Out] System.bool FrozenFeatureNeedsUpdate
)
```

### Parameters

- `FrozenFeatureNeedsUpdate`: True if the document has frozen features that need to be updated, false if not (see **Remarks**)

### Return Value

True if the document has frozen features, false if not

## VBA Syntax

See [SwDMDocument16::HasFrozenFeatures](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument16~HasFrozenFeatures.html).

## Examples

[Get Whether Part Has Frozen Features (C#)](Get_Whether_Part_Has_Frozen_Features_Example_CSharp.htm)
[Get Whether Part Has Frozen Features (VB.NET)](Get_Whether_Part_Has_Frozen_Features_Example_vbnet.htm)

## Remarks

The FrozenFeatureNeedsUpdate return value is only valid if the document has frozen features.

## See Also

[ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.html)
[ISwDMDocument16 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16_members.html)

## Availability

SOLIDWORKS Document Manager API 2012 SP0
