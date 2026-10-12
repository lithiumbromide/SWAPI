---
title: "AddAGroupOfFaces Method (ISMNormalCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData"
member: "AddAGroupOfFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~AddAGroupOfFaces.html"
---

# AddAGroupOfFaces Method (ISMNormalCutFeatureData)

Obsolete. See [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddAGroupOfFaces( _
   ByVal FaceArray As System.Object, _
   ByRef Error As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData
Dim FaceArray As System.Object
Dim Error As System.Integer

instance.AddAGroupOfFaces(FaceArray, Error)
```

### C#

```csharp
void AddAGroupOfFaces(
   System.object FaceArray,
   out System.int Error
)
```

### C++/CLI

```cpp
void AddAGroupOfFaces(
   System.Object^ FaceArray,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceArray`: Array of cut-extrude [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- `Error`: Error code as defined in [swSMNormalCutError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMNormalCutError_e.html)

## VBA Syntax

See [SMNormalCutFeatureData::AddAGroupOfFaces](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData~AddAGroupOfFaces.html).

## Examples

See the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.html) example.

## Remarks

FaceArray contains the non-normal side walls of a cut in a sheet metal part.

## See Also

[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.html)
[ISMNormalCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData_members.html)
[ISMNormalCutFeatureData::RemoveAGroupOfFaces Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~RemoveAGroupOfFaces.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
