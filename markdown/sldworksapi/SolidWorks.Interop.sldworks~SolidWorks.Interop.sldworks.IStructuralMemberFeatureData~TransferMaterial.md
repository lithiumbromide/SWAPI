---
title: "TransferMaterial Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "TransferMaterial"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~TransferMaterial.html"
---

# TransferMaterial Property (IStructuralMemberFeatureData)

Gets or sets whether to transfer the [material properties of a library profile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LibraryProfileMaterial.html) for this structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransferMaterial As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Boolean

instance.TransferMaterial = value

value = instance.TransferMaterial
```

### C#

```csharp
System.bool TransferMaterial {get; set;}
```

### C++/CLI

```cpp
property System.bool TransferMaterial {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to transfer the material properties of a library profile, false to not

## VBA Syntax

See [StructuralMemberFeatureData::TransferMaterial](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~TransferMaterial.html).

## Examples

[Insert Structural Weldments Using Custom Weldment Profile (C#)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_CSharp.htm)
[Insert Structural Weldments Using Custom Weldment Profile (VB.NET)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VBNET.htm)
[Insert Structural Weldments Using Custom Weldment Profile (VBA)](Insert_Structural_Weldments_Using_Custom_Weldment_Profile_Example_VB.htm)

## Remarks

You can transfer material properties of a library profile:

- when you use it as a structural member.
- that has a configuration-specific material.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)
[IStructuralMemberFeatureData::ConfigurationName Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConfigurationName.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
