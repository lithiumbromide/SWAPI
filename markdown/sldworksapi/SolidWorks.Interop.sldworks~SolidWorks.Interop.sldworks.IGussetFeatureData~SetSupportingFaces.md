---
title: "SetSupportingFaces Method (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "SetSupportingFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~SetSupportingFaces.html"
---

# SetSupportingFaces Method (IGussetFeatureData)

Sets the two, adjacent, supporting faces for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSupportingFaces( _
   ByVal PFace1 As Face2, _
   ByVal PFace2 As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim PFace1 As Face2
Dim PFace2 As Face2
Dim value As System.Boolean

value = instance.SetSupportingFaces(PFace1, PFace2)
```

### C#

```csharp
System.bool SetSupportingFaces(
   Face2 PFace1,
   Face2 PFace2
)
```

### C++/CLI

```cpp
System.bool SetSupportingFaces(
   Face2^ PFace1,
   Face2^ PFace2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFace1`: Pointer to the first [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object
- `PFace2`: Pointer to the second [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object

### Return Value

True if the supporting faces are set, false if not

## VBA Syntax

See [GussetFeatureData::SetSupportingFaces](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~SetSupportingFaces.html).

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)
[IGussetFeatureData::GetSupportingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~GetSupportingFaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
