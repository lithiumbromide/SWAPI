---
title: "SetCurrentProfile Method (CostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisStructural"
member: "SetCurrentProfile"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural~SetCurrentProfile.html"
---

# SetCurrentProfile Method (CostAnalysisStructural)

Sets the profile for the weldment in this Costing analysis for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurrentProfile( _
   ByVal Standard As System.String, _
   ByVal ProfileType As System.String, _
   ByVal ProfileSize As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisStructural
Dim Standard As System.String
Dim ProfileType As System.String
Dim ProfileSize As System.String
Dim value As System.Boolean

value = instance.SetCurrentProfile(Standard, ProfileType, ProfileSize)
```

### C#

```csharp
System.bool SetCurrentProfile(
   System.string Standard,
   System.string ProfileType,
   System.string ProfileSize
)
```

### C++/CLI

```cpp
System.bool SetCurrentProfile(
   System.String^ Standard,
   System.String^ ProfileType,
   System.String^ ProfileSize
)
```

### Parameters

- `Standard`: Name of the profile standard (see **Remarks**)
- `ProfileType`: Name of the profile type (see **Remarks**)
- `ProfileSize`: Profile size (see **Remarks**)

### Return Value

True if the profile is set, false if not (see **Remarks**)

## VBA Syntax

See [CostAnalysisStructural::SetCurrentProfile](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~SetCurrentProfile.html).

## Remarks

| A valid string for... | Corresponds to name of the... |
| --- | --- |
| Standard | Weldment profile folder, typically located in C:\Program Files\SolidWorks Corp\SOLIDWORKS \ lang \ lang \ weldment profiles |
| ProfileType | Profile types folder, typically located in C:\Program Files\SolidWorks Corp\SOLIDWORKS \ lang \ lang \ weldment profiles\ profile standard |
| ProfileSize | Profile size file, excluding the filename extension, typically located in C:\Program Files\SolidWorks Corp\SOLIDWORKS \ lang \ lang \ weldment profiles\ profile standard \ profile type |

This method:

- does not change the underlying geometry of the structural member; instead, this method only uses the specified profile to cost the body.
- fails if the specified Standard, ProfileType, or ProfileSize values are invalid or incompatible with each other.
- could invalidate the [cost method](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentCostMethodType.html).

## See Also

[CostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural.html)
[CostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisStructural_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
