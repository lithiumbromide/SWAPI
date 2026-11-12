---
title: "GetSaveStressAndReactionsOptions2 Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "GetSaveStressAndReactionsOptions2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSaveStressAndReactionsOptions2.html"
---

# GetSaveStressAndReactionsOptions2 Method (ICWStudyResultOptions)

Gets whether to save stress and reaction results and, if so, whether to save them for all stress components or nodal von Mises stresses only.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSaveStressAndReactionsOptions2( _
   ByRef BSaveStressAndReactions As System.Boolean, _
   ByRef BVonMisesOnly As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim BSaveStressAndReactions As System.Boolean
Dim BVonMisesOnly As System.Boolean
Dim value As System.Boolean

value = instance.GetSaveStressAndReactionsOptions2(BSaveStressAndReactions, BVonMisesOnly)
```

### C#

```csharp
System.bool GetSaveStressAndReactionsOptions2(
   out System.bool BSaveStressAndReactions,
   out System.bool BVonMisesOnly
)
```

### C++/CLI

```cpp
System.bool GetSaveStressAndReactionsOptions2(
   [Out] System.bool BSaveStressAndReactions,
   [Out] System.bool BVonMisesOnly
)
```

### Parameters

- `BSaveStressAndReactions`: -1 or true to save stress and reaction results, 0 or false to not
- `BVonMisesOnly`: -1 or true to save nodal von Mises stresses only, 0 to save all stress components; valid only if BSaveStressAndReactions is set to -1

### Return Value

-1 or true if successful, 0 or false if not

## Remarks

This method returns booleans or integers in the out parameters, depending on their prior declarations.

If out parameters are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
