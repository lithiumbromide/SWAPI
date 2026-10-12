---
title: "SetSaveStressAndReactionsOptions2 Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SetSaveStressAndReactionsOptions2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSaveStressAndReactionsOptions2.html"
---

# SetSaveStressAndReactionsOptions2 Method (ICWStudyResultOptions)

Sets whether to save stress and reaction results and, if so, whether to save them for all stress components or nodal von Mises stresses only.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSaveStressAndReactionsOptions2( _
   ByVal BSaveStressAndReactions As System.Boolean, _
   ByVal BVonMisesOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim BSaveStressAndReactions As System.Boolean
Dim BVonMisesOnly As System.Boolean
Dim value As System.Boolean

value = instance.SetSaveStressAndReactionsOptions2(BSaveStressAndReactions, BVonMisesOnly)
```

### C#

```csharp
System.bool SetSaveStressAndReactionsOptions2(
   System.bool BSaveStressAndReactions,
   System.bool BVonMisesOnly
)
```

### C++/CLI

```cpp
System.bool SetSaveStressAndReactionsOptions2(
   System.bool BSaveStressAndReactions,
   System.bool BVonMisesOnly
)
```

### Parameters

- `BSaveStressAndReactions`: -1 or true to save stress and reaction results, 0 or false to not
- `BVonMisesOnly`: -1 or true to save nodal von Mises stresses only, 0 or false to save all stress components; valid only if BSaveStressAndReactions is set to -1

### Return Value

True if successful, false if not

## Examples

See the [ICWStudyResultOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html) examples.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
