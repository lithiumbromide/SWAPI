---
title: "WeldmentProfilePath Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "WeldmentProfilePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~WeldmentProfilePath.html"
---

# WeldmentProfilePath Property (IStructuralMemberFeatureData)

Gets or sets the path for the profile for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property WeldmentProfilePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.String

instance.WeldmentProfilePath = value

value = instance.WeldmentProfilePath
```

### C#

```csharp
System.string WeldmentProfilePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ WeldmentProfilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Full path and filename for the profile (see Remarks)

## VBA Syntax

See [StructuralMemberFeatureData::WeldmentProfilePath](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~WeldmentProfilePath.html).

## Remarks

Weldment profiles are located in `install_dir`/lang/`lang`/weldment profiles subfolders and are named filename.sldflp.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::LocateProfilePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
