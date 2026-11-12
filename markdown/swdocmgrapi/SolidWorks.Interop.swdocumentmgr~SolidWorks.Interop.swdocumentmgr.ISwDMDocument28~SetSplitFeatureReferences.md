---
title: "SetSplitFeatureReferences Method (ISwDMDocument28)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument28"
member: "SetSplitFeatureReferences"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28~SetSplitFeatureReferences.html"
---

# SetSplitFeatureReferences Method (ISwDMDocument28)

Sets the specified split parts in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSplitFeatureReferences( _
   ByVal ListOfSplitPartPaths As System.Object, _
   ByVal ListOfModifiedSplitPartPaths As System.Object, _
   ByVal NewPathName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument28
Dim ListOfSplitPartPaths As System.Object
Dim ListOfModifiedSplitPartPaths As System.Object
Dim NewPathName As System.String

instance.SetSplitFeatureReferences(ListOfSplitPartPaths, ListOfModifiedSplitPartPaths, NewPathName)
```

### C#

```csharp
void SetSplitFeatureReferences(
   System.object ListOfSplitPartPaths,
   System.object ListOfModifiedSplitPartPaths,
   System.string NewPathName
)
```

### C++/CLI

```cpp
void SetSplitFeatureReferences(
   System.Object^ ListOfSplitPartPaths,
   System.Object^ ListOfModifiedSplitPartPaths,
   System.String^ NewPathName
)
```

### Parameters

- `ListOfSplitPartPaths`: Array of paths of split parts
- `ListOfModifiedSplitPartPaths`: Array of renamed paths of split parts
- `NewPathName`: New path name

## VBA Syntax

See [SwDMDocument28::SetSplitFeatureReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument28~SetSplitFeatureReferences.html).

## Remarks

SOLIDWORKS 2022 allows you to Pack and Go parts created by the Save Bodies and Split features. The split parts created are listed as references of the parent part.

## See Also

[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.html)
[ISwDMDocument28 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28_members.html)

## Availability

SOLIDWORKS Document Manager API 2022 SP0
