---
title: "GetCoordinateSystemTransformByName Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCoordinateSystemTransformByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html"
---

# GetCoordinateSystemTransformByName Method (IModelDocExtension)

Gets the transform of the specified coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoordinateSystemTransformByName( _
   ByVal NameIn As System.String _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NameIn As System.String
Dim value As MathTransform

value = instance.GetCoordinateSystemTransformByName(NameIn)
```

### C#

```csharp
MathTransform GetCoordinateSystemTransformByName(
   System.string NameIn
)
```

### C++/CLI

```cpp
MathTransform^ GetCoordinateSystemTransformByName(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Name of the coordinate system

### Return Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [ModelDocExtension::GetCoordinateSystemTransformByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCoordinateSystemTransformByName.html).

## Examples

[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)
[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::GetCurrentCoordinateSystemName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.html)
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.html)

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
