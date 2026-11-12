---
title: "GetFeature Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature.html"
---

# GetFeature Method (IFace2)

Gets the feature that owns this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetFeature()
```

### C#

```csharp
System.object GetFeature()
```

### C++/CLI

```cpp
System.Object^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Owning [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Face2::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetFeature.html).

## Examples

[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)
[Get Faces Associated with Feature (C#)](Get_Faces_Associated_with_Feature_Example_CSharp.htm)
[Get Faces Associated with Feature (VB.NET)](Get_Faces_Associated_with_Feature_Example_VBNET.htm)
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)

## Remarks

In SOLIDWORKS, a face:

- is the result of evaluating a feature.
- can be owned by several features.

[IFeature::GetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaces.html) or [IFeature::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html) returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

To filter out multiple feature faces using the SOLIDWORKS API, you must call IFace2::GetFeature or [IFace2::IGetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFeature.html). Only the oldest feature from the face is returned, that is, the first owning feature in the FeatureManager design tree.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetFeatureId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeatureId.html)
[IFace2::IGetFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
