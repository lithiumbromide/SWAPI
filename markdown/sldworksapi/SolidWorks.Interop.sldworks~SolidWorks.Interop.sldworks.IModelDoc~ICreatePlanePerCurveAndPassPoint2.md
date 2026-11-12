---
title: "ICreatePlanePerCurveAndPassPoint2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreatePlanePerCurveAndPassPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePlanePerCurveAndPassPoint2.html"
---

# ICreatePlanePerCurveAndPassPoint2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreatePlanePerCurveAndPassPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlanePerCurveAndPassPoint2( _
   ByVal OrigAtCurve As System.Boolean _
) As RefPlane
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim OrigAtCurve As System.Boolean
Dim value As RefPlane

value = instance.ICreatePlanePerCurveAndPassPoint2(OrigAtCurve)
```

### C#

```csharp
RefPlane ICreatePlanePerCurveAndPassPoint2(
   System.bool OrigAtCurve
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlanePerCurveAndPassPoint2(
   System.bool OrigAtCurve
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OrigAtCurve`:

## VBA Syntax

See [ModelDoc::ICreatePlanePerCurveAndPassPoint2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreatePlanePerCurveAndPassPoint2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
