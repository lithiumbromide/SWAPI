---
title: "SetTrimToolMember Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "SetTrimToolMember"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~SetTrimToolMember.html"
---

# SetTrimToolMember Method (IComplexCornerTreatmentFeatureData)

Sets the trim tool member for this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTrimToolMember( _
   ByVal Member As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim Member As System.Object
Dim value As System.Boolean

value = instance.SetTrimToolMember(Member)
```

### C#

```csharp
System.bool SetTrimToolMember(
   System.object Member
)
```

### C++/CLI

```cpp
System.bool SetTrimToolMember(
   System.Object^ Member
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Member`: [ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

### Return Value

True if trim tool member successfully set, false if not

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::SetTrimToolMember](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~SetTrimToolMember.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
