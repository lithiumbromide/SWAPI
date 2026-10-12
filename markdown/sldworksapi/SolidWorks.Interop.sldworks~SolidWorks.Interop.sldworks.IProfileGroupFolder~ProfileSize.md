---
title: "ProfileSize Property (IProfileGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "IProfileGroupFolder"
member: "ProfileSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileSize.html"
---

# ProfileSize Property (IProfileGroupFolder)

Gets the profile size for this member profile group.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ProfileSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileGroupFolder
Dim value As System.String

value = instance.ProfileSize
```

### C#

```csharp
System.string ProfileSize {get;}
```

### C++/CLI

```cpp
property System.String^ ProfileSize {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Weldment profile size as defined in a weldment profile

## VBA Syntax

See [ProfileGroupFolder::ProfileSize](ms-its:sldworksapivb6.chm::/sldworks~ProfileGroupFolder~ProfileSize.html).

## Remarks

This property:

- is valid only if a [IProfileGroupFolder::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~ProfileType.html) is set.
- may be overridden by [IStructureSystemMemberProfile::ProfileSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileSize.html) for individual members.

Specify this property using strings found in:

- SOLIDWORKS-supplied weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang_name`\**weldment profiles
  -** or -
- custom weldment profile (*.**sldlfp**); see the SOLIDWORKS Help for details about custom weldment profiles

## See Also

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.html)
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
