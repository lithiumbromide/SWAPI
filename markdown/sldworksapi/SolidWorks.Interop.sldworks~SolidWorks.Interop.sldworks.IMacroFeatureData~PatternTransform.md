---
title: "PatternTransform Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "PatternTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PatternTransform.html"
---

# PatternTransform Property (IMacroFeatureData)

Gets the pattern transform.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternTransform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As MathTransform

value = instance.PatternTransform
```

### C#

```csharp
MathTransform PatternTransform {get;}
```

### C++/CLI

```cpp
property MathTransform^ PatternTransform {
   MathTransform^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [MacroFeatureData::PatternTransform](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~PatternTransform.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEditTargetTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform.html)
[IMacroFeatureData::FeatureTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~FeatureTransform.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
