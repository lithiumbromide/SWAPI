---
title: "IReferenceCurve Interface"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html"
---

# IReferenceCurve Interface

Allows access to reference curves.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IReferenceCurve
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
```

### C#

```csharp
public interface IReferenceCurve
```

### C++/CLI

```cpp
public interface class IReferenceCurve
```

## VBA Syntax

See [ReferenceCurve](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve.html).

## Examples

[Get Curve Segments (VBA)](Get_Curve_Segments_Example_VB.htm)
[Get Reference Curve Information (VBA)](Get_Reference_Curve_Information_Example_VB.htm)
[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

## Remarks

This includes the following types of curve features:

- 3D spline curves
- Curves from file
- Helix curves
- Imported curves

IReferenceCurve does not expose reference curve features (for example, projected curves).

## Accessors

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IModelDoc2::FeatureReferenceCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.html)

## Access Diagram

[ReferenceCurve](SWObjectModel.pdf#ReferenceCurve)

## See Also

[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
