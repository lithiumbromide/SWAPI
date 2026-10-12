---
title: "IGetMaterialPropertyValuesForFace Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetMaterialPropertyValuesForFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html"
---

# IGetMaterialPropertyValuesForFace Method (IBody2)

Gets the color of the specified face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterialPropertyValuesForFace( _
   ByVal FaceIn As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceIn As System.Object
Dim value As System.Double

value = instance.IGetMaterialPropertyValuesForFace(FaceIn)
```

### C#

```csharp
System.double IGetMaterialPropertyValuesForFace(
   System.object FaceIn
)
```

### C++/CLI

```cpp
System.double IGetMaterialPropertyValuesForFace(
   System.Object^ FaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceIn`: Face from which to get its color

### Return Value

Color of the face

## VBA Syntax

See [Body2::IGetMaterialPropertyValuesForFace](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetMaterialPropertyValuesForFace.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IComponent2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValuesForFace.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
