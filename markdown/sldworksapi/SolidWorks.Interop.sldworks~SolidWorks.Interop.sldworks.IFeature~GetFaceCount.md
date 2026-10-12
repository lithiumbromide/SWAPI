---
title: "GetFaceCount Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount.html"
---

# GetFaceCount Method (IFeature)

Gets the number of faces in this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetFaceCount()
```

### C#

```csharp
System.int GetFaceCount()
```

### C++/CLI

```cpp
System.int GetFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces in this feature

## VBA Syntax

See [Feature::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetFaceCount.html).

## Examples

[Get Faces Affected by Draft Feature (VBA)](Get_Faces_Affected_by_Draft_Feature_Example_VB.htm)
[Get Faces Affected by Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)
[Get Faces Associated with Feature (C#)](Get_Faces_Associated_with_Feature_Example_CSharp.htm)
[Get Faces Associated with Feature (VB.NET)](Get_Faces_Associated_with_Feature_Example_VBNET.htm)
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IFeature::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html).

A face:

- is the result of evaluating a feature.
- can be owned by several features.

This method returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

NOTES:

- This method does not return any faces for draft features because draft features do not create any new faces. Drafting only modifies existing faces.
- The number of faces for rolled hems is 0 because all of the faces belong to the children bends.

To filter out multiple feature faces, call [IFace2::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFeature.html) or [IFace2::IGetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFeature.html). Only the oldest feature from the face is returned; that is, the first owning feature in the FeatureManager design tree.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFace2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.html)
