---
title: "ProfileType Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileType.html"
---

# ProfileType Property (IStructureSystemMemberProfile)

Gets the profile type for this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.String

instance.ProfileType = value

value = instance.ProfileType
```

### C#

```csharp
System.string ProfileType {get; set;}
```

### C++/CLI

```cpp
property System.String^ ProfileType {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weldment profile type as defined in a weldment profile

## VBA Syntax

See [StructureSystemMemberProfile::ProfileType](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileType.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## Remarks

This property:

- is valid only if a [IStructureSystemMemberProfile::ProfileStandard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileStandard.html) is set.
- overrides [IProfileGroupFolder::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileType.html).

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang_name`\**weldment profiles
  -** or -
- custom weldment profile (*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
