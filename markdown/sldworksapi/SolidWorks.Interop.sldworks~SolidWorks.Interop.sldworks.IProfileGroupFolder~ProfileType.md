---
title: "ProfileType Property (IProfileGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "IProfileGroupFolder"
member: "ProfileType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileType.html"
---

# ProfileType Property (IProfileGroupFolder)

Gets the profile type for this member profile group.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ProfileType As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileGroupFolder
Dim value As System.String

value = instance.ProfileType
```

### C#

```csharp
System.string ProfileType {get;}
```

### C++/CLI

```cpp
property System.String^ ProfileType {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weldment profile type as defined in a weldment profile

## VBA Syntax

See [ProfileGroupFolder::ProfileType](ms-its:sldworksapivb6.chm::/sldworks~ProfileGroupFolder~ProfileType.html).

## Remarks

This property:

- is valid only if a [IProfileGroupFolder::ProfileStandard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileStandard.html) is set.
- may be overridden by [IStructureSystemMemberProfile::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileType.html) for individual members.

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang_name`\**weldment profiles
  -** or -
- custom weldment profile (*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

## See Also

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html)
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
