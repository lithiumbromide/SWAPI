---
title: "IGetFaces2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.html"
---

# IGetFaces2 Method (IFeature)

Gets the faces in this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces2( _
   ByRef FaceCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim FaceCount As System.Integer
Dim value As Face2

value = instance.IGetFaces2(FaceCount)
```

### C#

```csharp
Face2 IGetFaces2(
   out System.int FaceCount
)
```

### C++/CLI

```cpp
Face2^ IGetFaces2(
   [Out] System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces in this feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of pointers to the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To determine the size of the array, call [IFeature::GetFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaceCount.html) before calling this method.

IFeature::IGetFaces2 compares the number of faces in this feature with FaceCount. If the actual number of faces is larger than the specified FaceCount, then this method returns no faces and a status of S_ERROR. If the actual number of faces is smaller than the specified in FaceCount, then this method returns all of the faces in the return array, and changes FaceCount to reflect the correct number of faces.

In SOLIDWORKS, a face:

- is the result of evaluating a feature.
- can be owned by several features.

IFeature::IGetFaces2 returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

NOTES:

- This method does not return any faces for draft features because draft features do not create any new faces. Drafting only modifies existing faces.
- The number of faces for rolled hems is 0 because all of the faces belong to the children bends.

To filter out multiple feature faces using the SOLIDWORKS API, you must call [IFace2::IGetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFeature.html). Only the oldest feature from the face is returned, that is, the first owning feature in the FeatureManager design tree.

**Example**

```vb
HRESULT    hr = S_OK;
long       lNumFaces = 0;

hr = feat->GetFaceCount(&lNumFaces);

LPFACE2*   aFaces = new LPFACE2[lNumFaces];

hr = feat->IGetFaces2(&lNumFaces, aFaces);

...

delete [] aFaces;
aFaces = 0;
```

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
