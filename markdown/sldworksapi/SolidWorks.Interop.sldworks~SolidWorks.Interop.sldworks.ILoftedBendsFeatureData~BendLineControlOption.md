---
title: "BendLineControlOption Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "BendLineControlOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~BendLineControlOption.html"
---

# BendLineControlOption Property (ILoftedBendsFeatureData)

Gets or sets the lofted bend line control options.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendLineControlOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer

instance.BendLineControlOption = value

value = instance.BendLineControlOption
```

### C#

```csharp
System.int BendLineControlOption {get; set;}
```

### C++/CLI

```cpp
property System.int BendLineControlOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Lofted bend line control options as defined in [swBendLineControlOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendLineControlOption_e.html)

## VBA Syntax

See [LoftedBendsFeatureData::BendLineControlOption](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~BendLineControlOption.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::CanCreateBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~CanCreateBendLines.html)
[ILoftedBendsFeatureData::MaximumDeviation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~MaximumDeviation.html)
[ILoftedBendsFeatureData::NumberOfBendLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~NumberOfBendLines.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
