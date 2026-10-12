---
title: "ProfileStandard Property (IProfileGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "IProfileGroupFolder"
member: "ProfileStandard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileStandard.html"
---

# ProfileStandard Property (IProfileGroupFolder)

Gets the profile standard for this member profile group.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ProfileStandard As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileGroupFolder
Dim value As System.String

value = instance.ProfileStandard
```

### C#

```csharp
System.string ProfileStandard {get;}
```

### C++/CLI

```cpp
property System.String^ ProfileStandard {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weldment profile standard as defined in a weldment profile

## VBA Syntax

See [ProfileGroupFolder::ProfileStandard](ms-its:sldworksapivb6.chm::/sldworks~ProfileGroupFolder~ProfileStandard.html).

## Remarks

This property may be overridden by [IStructureSystemMemberProfile::ProfileStandard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileStandard.html) for individual members.

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang_name`\**weldment profiles
  -** or -
- custom weldment profile (*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

## See Also

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html)
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
