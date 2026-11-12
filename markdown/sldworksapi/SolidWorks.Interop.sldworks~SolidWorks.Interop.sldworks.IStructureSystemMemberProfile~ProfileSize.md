---
title: "ProfileSize Property (IStructureSystemMemberProfile)"
project: "SOLIDWORKS API Help"
interface: "IStructureSystemMemberProfile"
member: "ProfileSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileSize.html"
---

# ProfileSize Property (IStructureSystemMemberProfile)

Gets the profile size for this member profile.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStructureSystemMemberProfile
Dim value As System.String

instance.ProfileSize = value

value = instance.ProfileSize
```

### C#

```csharp
System.string ProfileSize {get; set;}
```

### C++/CLI

```cpp
property System.String^ ProfileSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weldment profile size as defined in a weldment profile

## VBA Syntax

See [StructureSystemMemberProfile::ProfileSize](ms-its:sldworksapivb6.chm::/sldworks~StructureSystemMemberProfile~ProfileSize.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## Remarks

This property:

- is valid only if a [IStructureSystemMemberProfile::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileType.html) is set.
- overrides [IProfileGroupFolder::ProfileSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileSize.html).

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang_name`\**weldment profiles
  -** or -
- custom weldment profile (*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

## See Also

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.html)
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
