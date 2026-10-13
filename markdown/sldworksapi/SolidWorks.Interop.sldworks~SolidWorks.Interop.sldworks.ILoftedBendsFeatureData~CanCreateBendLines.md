---
title: "CanCreateBendLines Method (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "CanCreateBendLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.html"
---

# CanCreateBendLines Method (ILoftedBendsFeatureData)

Gets whether the bend lines parameters affect this lofted bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function CanCreateBendLines() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean

value = instance.CanCreateBendLines()
```

### C#

```csharp
System.bool CanCreateBendLines()
```

### C++/CLI

```cpp
System.bool CanCreateBendLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if bend lines parameters affect this lofted bend feature, false if not

## VBA Syntax

See [LoftedBendsFeatureData::CanCreateBendLines](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~CanCreateBendLines.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.html)
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.html)
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
