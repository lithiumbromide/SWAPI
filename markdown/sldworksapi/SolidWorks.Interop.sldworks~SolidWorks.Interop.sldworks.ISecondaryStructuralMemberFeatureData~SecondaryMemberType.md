---
title: "SecondaryMemberType Property (ISecondaryStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryStructuralMemberFeatureData"
member: "SecondaryMemberType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData~SecondaryMemberType.html"
---

# SecondaryMemberType Property (ISecondaryStructuralMemberFeatureData)

Gets the type of this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SecondaryMemberType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryStructuralMemberFeatureData
Dim value As System.Integer

value = instance.SecondaryMemberType
```

### C#

```csharp
System.int SecondaryMemberType {get;}
```

### C++/CLI

```cpp
property System.int SecondaryMemberType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Secondary structure system member type as defined by [swStructureSystemMemberCreationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSystemMemberCreationType_e.html)

## VBA Syntax

See [SecondaryStructuralMemberFeatureData::SecondaryMemberType](ms-its:sldworksapivb6.chm::/sldworks~SecondaryStructuralMemberFeatureData~SecondaryMemberType.html).

## Examples

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html) examples.

## See Also

[ISecondaryStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData.html)
[ISecondaryStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
