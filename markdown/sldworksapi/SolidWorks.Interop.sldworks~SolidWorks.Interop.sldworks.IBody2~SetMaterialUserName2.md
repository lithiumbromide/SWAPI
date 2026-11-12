---
title: "SetMaterialUserName2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "SetMaterialUserName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html"
---

# SetMaterialUserName2 Method (IBody2)

Sets the material name for this body. This material name is visible to the user.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialUserName2( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialUserName2(Name)
```

### C#

```csharp
System.bool SetMaterialUserName2(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialUserName2(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Material name

### Return Value

True if the material name is set successfully, false if not

## VBA Syntax

See [Body2::SetMaterialUserName2](ms-its:sldworksapivb6.chm::/sldworks~Body2~SetMaterialUserName2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
