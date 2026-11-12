---
title: "SetBodyTrimMembers Method (IComplexCornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: "SetBodyTrimMembers"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~SetBodyTrimMembers.html"
---

# SetBodyTrimMembers Method (IComplexCornerTreatmentFeatureData)

Sets the body trim members of this complex corner treatment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBodyTrimMembers( _
   ByVal BodyMemList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
Dim BodyMemList As System.Object
Dim value As System.Boolean

value = instance.SetBodyTrimMembers(BodyMemList)
```

### C#

```csharp
System.bool SetBodyTrimMembers(
   System.object BodyMemList
)
```

### C++/CLI

```cpp
System.bool SetBodyTrimMembers(
   System.Object^ BodyMemList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyMemList`: Array of body trim [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html)s

### Return Value

True if body trim members successfully set, false if not

## VBA Syntax

See [ComplexCornerTreatmentFeatureData::SetBodyTrimMembers](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData~SetBodyTrimMembers.html).

## See Also

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html)
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
