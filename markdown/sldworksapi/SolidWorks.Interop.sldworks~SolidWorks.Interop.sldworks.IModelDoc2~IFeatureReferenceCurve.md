---
title: "IFeatureReferenceCurve Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IFeatureReferenceCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve.html"
---

# IFeatureReferenceCurve Method (IModelDoc2)

Creates a reference curve feature from an array of curves.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByRef BaseCurves As Curve, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As ReferenceCurve
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NumOfCurves As System.Integer
Dim BaseCurves As Curve
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As ReferenceCurve

value = instance.IFeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

### C#

```csharp
ReferenceCurve IFeatureReferenceCurve(
   System.int NumOfCurves,
   ref Curve BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
ReferenceCurve^ IFeatureReferenceCurve(
   System.int NumOfCurves,
   Curve^% BaseCurves,
   System.bool Merge,
   System.String^ FromFileName,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfCurves`: Number of curves from which to create the object
- `BaseCurves`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `Merge`: True creates a single reference curve feature, false creates a reference curve feature for each curve in the array
- `FromFileName`: Not used
- `ErrorCode`: Error code as defined in [swFeatureError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

### Return Value

[Reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html)

## VBA Syntax

See [ModelDoc2::IFeatureReferenceCurve](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IFeatureReferenceCurve.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::FeatureReferenceCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.html)
