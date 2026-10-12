---
title: "GetSplitFeatureReferences Method (ISwDMDocument28)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument28"
member: "GetSplitFeatureReferences"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~GetSplitFeatureReferences.html"
---

# GetSplitFeatureReferences Method (ISwDMDocument28)

Gets the split parts in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitFeatureReferences( _
   ByVal SrcOption As SwDMSearchOption _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument28
Dim SrcOption As SwDMSearchOption
Dim value As System.Object

value = instance.GetSplitFeatureReferences(SrcOption)
```

### C#

```csharp
System.object GetSplitFeatureReferences(
   SwDMSearchOption SrcOption
)
```

### C++/CLI

```cpp
System.Object^ GetSplitFeatureReferences(
   SwDMSearchOption^ SrcOption
)
```

### Parameters

- `SrcOption`: [ISwDMSearchOption](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)

### Return Value

Array of paths of split parts

## VBA Syntax

See [SwDMDocument28::GetSplitFeatureReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument28~GetSplitFeatureReferences.html).

## Remarks

SOLIDWORKS 2022 allows you to Pack and Go parts created by the Save Bodies and Split features. The split parts created are listed as references of the parent part.

## See Also

[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.html)
[ISwDMDocument28 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28_members.html)

## Availability

SOLIDWORKS Document Manager API 2022 SP0
