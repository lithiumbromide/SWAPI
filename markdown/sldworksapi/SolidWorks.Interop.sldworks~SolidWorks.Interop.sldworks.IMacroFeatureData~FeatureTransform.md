---
title: "FeatureTransform Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "FeatureTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~FeatureTransform.html"
---

# FeatureTransform Property (IMacroFeatureData)

Gets and sets the macro feature transform.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureTransform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As MathTransform

instance.FeatureTransform = value

value = instance.FeatureTransform
```

### C#

```csharp
MathTransform FeatureTransform {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ FeatureTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [MacroFeatureData::FeatureTransform](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~FeatureTransform.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetEditTargetTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEditTargetTransform.html)
[IMacroFeatureData::PatternTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PatternTransform.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
