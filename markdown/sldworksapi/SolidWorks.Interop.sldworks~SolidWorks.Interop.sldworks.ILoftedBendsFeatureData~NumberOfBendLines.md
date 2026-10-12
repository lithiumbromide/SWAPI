---
title: "NumberOfBendLines Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "NumberOfBendLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.html"
---

# NumberOfBendLines Property (ILoftedBendsFeatureData)

Gets or sets the number of bend lines in this lofted bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfBendLines As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer

instance.NumberOfBendLines = value

value = instance.NumberOfBendLines
```

### C#

```csharp
System.int NumberOfBendLines {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfBendLines {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of bend lines in this lofted bend feature

## VBA Syntax

See [LoftedBendsFeatureData::NumberOfBendLines](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~NumberOfBendLines.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.html)
[ILoftedBendsFeatureData::BendLineControlOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.html)
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
