---
title: "GetUnderlyingMemberFeature Method (ICornerMember)"
project: "SOLIDWORKS API Help"
interface: "ICornerMember"
member: "GetUnderlyingMemberFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~GetUnderlyingMemberFeature.html"
---

# GetUnderlyingMemberFeature Method (ICornerMember)

Gets the feature for this corner member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUnderlyingMemberFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerMember
Dim value As System.Object

value = instance.GetUnderlyingMemberFeature()
```

### C#

```csharp
System.object GetUnderlyingMemberFeature()
```

### C++/CLI

```cpp
System.Object^ GetUnderlyingMemberFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [CornerMember::GetUnderlyingMemberFeature](ms-its:sldworksapivb6.chm::/sldworks~CornerMember~GetUnderlyingMemberFeature.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

After calling this method to get the IFeature, use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to get an [ISructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.html).

## See Also

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html)
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
