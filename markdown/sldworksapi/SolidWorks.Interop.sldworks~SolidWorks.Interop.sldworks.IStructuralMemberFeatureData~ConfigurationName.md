---
title: "ConfigurationName Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "ConfigurationName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName.html"
---

# ConfigurationName Property (IStructuralMemberFeatureData)

Gets or sets the name of the configuration in the custom weldment profile for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.String

instance.ConfigurationName = value

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the configuration in the custom weldment profile or an empty string (see **Remarks**)

## VBA Syntax

See [StructuralMemberFeatureData::ConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~ConfigurationName.html).

## Examples

[Insert Structural Weldments Using Custom Weldment Profile (C#)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_CSharp.htm)
[Insert Structural Weldments Using Custom Weldment Profile (VB.NET)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VBNET.htm)
[Insert Structural Weldments Using Custom Weldment Profile (VBA)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VB.htm)

## Remarks

An empty string indicates that a configuration in a custom weldment profile was not used for this structural member.

See:

- [IFeatureManager::InsertStructuralWeldment5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment5.html) for details about inserting a structural member using a configuration in a custom weldment profile.
- SOLIDWORKS Help for details about custom weldment profiles.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
