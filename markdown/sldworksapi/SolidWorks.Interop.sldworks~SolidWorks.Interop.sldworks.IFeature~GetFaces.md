---
title: "GetFaces Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.html"
---

# GetFaces Method (IFeature)

Gets the faces in this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaces() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetFaces()
```

### C#

```csharp
System.object GetFaces()
```

### C++/CLI

```cpp
System.Object^ GetFaces();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [Feature::GetFaces](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetFaces.html).

## Examples

[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)
[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

## Remarks

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
[IFeature::IGetFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.html)
[IFeature::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount.html)
