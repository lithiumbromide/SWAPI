---
title: "GetCSYSXYZAngularRotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCSYSXYZAngularRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSXYZAngularRotation.html"
---

# GetCSYSXYZAngularRotation Method (IModelDocExtension)

Gets the specified Tait-Bryan angular rotation values that transform one selected coordinate system into another.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCSYSXYZAngularRotation( _
   ByRef XAngle As System.Double, _
   ByRef YAngle As System.Double, _
   ByRef ZAngle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim XAngle As System.Double
Dim YAngle As System.Double
Dim ZAngle As System.Double
Dim value As System.Boolean

value = instance.GetCSYSXYZAngularRotation(XAngle, YAngle, ZAngle)
```

### C#

```csharp
System.bool GetCSYSXYZAngularRotation(
   out System.double XAngle,
   out System.double YAngle,
   out System.double ZAngle
)
```

### C++/CLI

```cpp
System.bool GetCSYSXYZAngularRotation(
   [Out] System.double XAngle,
   [Out] System.double YAngle,
   [Out] System.double ZAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XAngle`: Angle of rotation between x axes
- `YAngle`: Angle of rotation between y axes
- `ZAngle`: Angle of rotation between z axes

### Return Value

True if rotation values successfully retrieved, false if not

## VBA Syntax

See [ModelDocExtension::GetCSYSXYZAngularRotation](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetCSYSXYZAngularRotation.html).

## Remarks

This method corresponds to the SOLIDWORKS measure tool's calculation of angular rotation between two coordinate systems. See **SOLIDWORKS online help > Fundamentals > Measure Tool** for more information.

Use Wikipedia to learn about Tait-Bryan or Cardan angles.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCSYSDistances Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSDistances.html)
[IModelDocExtension::GetCSYSEulersAngularRotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCSYSEulersAngularRotation.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
