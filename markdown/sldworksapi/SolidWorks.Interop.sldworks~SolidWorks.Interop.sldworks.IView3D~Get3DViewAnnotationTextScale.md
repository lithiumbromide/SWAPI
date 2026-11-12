---
title: "Get3DViewAnnotationTextScale Method (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Get3DViewAnnotationTextScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Get3DViewAnnotationTextScale.html"
---

# Get3DViewAnnotationTextScale Method (IView3D)

Gets the annotation text scale for this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Get3DViewAnnotationTextScale( _
   ByRef Scale1 As System.Double, _
   ByRef Scale2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim Scale1 As System.Double
Dim Scale2 As System.Double

instance.Get3DViewAnnotationTextScale(Scale1, Scale2)
```

### C#

```csharp
void Get3DViewAnnotationTextScale(
   out System.double Scale1,
   out System.double Scale2
)
```

### C++/CLI

```cpp
void Get3DViewAnnotationTextScale(
   [Out] System.double Scale1,
   [Out] System.double Scale2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Scale1`: Numerator of the scale ratio (**n**:n)
- `Scale2`: Denominator of the scale ratio (n:**n**)

## VBA Syntax

See [View3D::Get3DViewAnnotationTextScale](ms-its:sldworksapivb6.chm::/sldworks~View3D~Get3DViewAnnotationTextScale.html).

## Remarks

This method gets the **Text scale** on the Annotation Properties dialog that appears when you RMB on the Annotations folder in the FeatureManager design tree.

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
