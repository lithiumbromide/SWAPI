---
title: "IGetMaterialPropertyValuesForFace Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetMaterialPropertyValuesForFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValuesForFace.html"
---

# IGetMaterialPropertyValuesForFace Method (IComponent2)

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
Dim instance As IComponent2
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

- `FaceIn`: Pointer to the face from which to get its color

### Return Value

Color of the face

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
