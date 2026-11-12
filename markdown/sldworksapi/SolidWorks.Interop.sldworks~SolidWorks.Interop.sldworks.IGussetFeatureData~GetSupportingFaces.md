---
title: "GetSupportingFaces Method (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "GetSupportingFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~GetSupportingFaces.html"
---

# GetSupportingFaces Method (IGussetFeatureData)

Gets the two, adjacent, supporting faces for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSupportingFaces( _
   ByRef PFace1 As Face2, _
   ByRef PFace2 As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim PFace1 As Face2
Dim PFace2 As Face2
Dim value As System.Boolean

value = instance.GetSupportingFaces(PFace1, PFace2)
```

### C#

```csharp
System.bool GetSupportingFaces(
   out Face2 PFace1,
   out Face2 PFace2
)
```

### C++/CLI

```cpp
System.bool GetSupportingFaces(
   [Out] Face2^ PFace1,
   [Out] Face2^ PFace2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PFace1`: Pointer to the first [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object
- `PFace2`: Pointer to the second [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object

### Return Value

True if both faces are returned, false if not

## VBA Syntax

See [GussetFeatureData::GetSupportingFaces](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~GetSupportingFaces.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)
[IGussetFeatureData::SetSupportingFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~SetSupportingFaces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
