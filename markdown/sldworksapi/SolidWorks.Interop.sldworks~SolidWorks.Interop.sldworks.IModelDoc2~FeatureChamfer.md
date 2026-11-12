---
title: "FeatureChamfer Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamfer.html"
---

# FeatureChamfer Method (IModelDoc2)

Creates a chamfer feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureChamfer( _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean

instance.FeatureChamfer(Width, Angle, Flip)
```

### C#

```csharp
void FeatureChamfer(
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

### C++/CLI

```cpp
void FeatureChamfer(
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the chamfer in meters
- `Angle`: Angle of the chamfer
- `Flip`: - 0 if angle is to be measured from the right face
  - 1 if angle is to be measured from the left face

## VBA Syntax

See [ModelDoc2::FeatureChamfer](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureChamfer.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
