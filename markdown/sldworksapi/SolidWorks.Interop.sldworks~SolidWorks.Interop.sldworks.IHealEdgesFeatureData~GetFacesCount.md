---
title: "GetFacesCount Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "GetFacesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~GetFacesCount.html"
---

# GetFacesCount Method (IHealEdgesFeatureData)

Gets the number of faces for this heal edges feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim value As System.Integer

value = instance.GetFacesCount()
```

### C#

```csharp
System.int GetFacesCount()
```

### C++/CLI

```cpp
System.int GetFacesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [HealEdgesFeatureData::GetFacesCount](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~GetFacesCount.html).

## Examples

[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## Remarks

Call this method before calling [IHealEdgesFeatureData::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHealEdgesFeatureData~IGetFaces.html).

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
