---
title: "GetSphericalBoxDiameter Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSphericalBoxDiameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSphericalBoxDiameter.html"
---

# GetSphericalBoxDiameter Method (IModelDocExtension)

Gets the diameter of the spherical bounding box of this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSphericalBoxDiameter() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Double

value = instance.GetSphericalBoxDiameter()
```

### C#

```csharp
System.double GetSphericalBoxDiameter()
```

### C++/CLI

```cpp
System.double GetSphericalBoxDiameter();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Diameter of the sphere that encloses this model's bounding box

## VBA Syntax

See [ModelDocExtension::GetSphericalBoxDiameter](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSphericalBoxDiameter.html).

## Examples

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html) examples.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
