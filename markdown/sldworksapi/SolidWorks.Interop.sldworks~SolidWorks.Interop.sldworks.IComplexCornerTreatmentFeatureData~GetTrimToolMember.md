---
title: "GetTrimToolMember Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "GetTrimToolMember"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.html"
---

# GetTrimToolMember Method (IComplexCornerTreatmentFeatureData)

Gets the specified trim tool member for this complex corner treatment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimToolMember( _
   ByRef MemberObjType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim MemberObjType As System.Integer
Dim value As System.Object

value = instance.GetTrimToolMember(MemberObjType)
```

### C#

```csharp
System.object GetTrimToolMember(
   out System.int MemberObjType
)
```

### C++/CLI

```cpp
System.Object^ GetTrimToolMember(
   [Out] System.int MemberObjType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MemberObjType`: Trim tool member object to return as defined by [swTrimToolMemberObjectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTrimToolMemberObjectType_e.html)

### Return Value

[ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::GetTrimToolMember](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~GetTrimToolMember.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
