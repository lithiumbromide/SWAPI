---
title: "GetPathType Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetPathType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.html"
---

# GetPathType Method (ISweepFeatureData)

Gets the path type for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

value = instance.GetPathType()
```

### C#

```csharp
System.int GetPathType()
```

### C++/CLI

```cpp
System.int GetPathType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sweep path type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SweepFeatureData::GetPathType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetPathType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.html)
[ISweepFeatureData::SetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.html)
[ISweepFeatureData::Path Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.html)
[ISweepFeatureData::PathAlignmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html)
[ISweepFeatureData::StartTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~StartTangencyType.html)
[ISweepFeatureData::EndTangencyType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~EndTangencyType.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
