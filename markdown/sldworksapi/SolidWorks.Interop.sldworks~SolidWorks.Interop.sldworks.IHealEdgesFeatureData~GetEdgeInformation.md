---
title: "GetEdgeInformation Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "GetEdgeInformation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~GetEdgeInformation.html"
---

# GetEdgeInformation Method (IHealEdgesFeatureData)

Gets the number of edges before healing and the number of edges after healing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetEdgeInformation( _
   ByRef EdgeCountBefore As System.Integer, _
   ByRef EdgeCountAfter As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IHealEdgesFeatureData
Dim EdgeCountBefore As System.Integer
Dim EdgeCountAfter As System.Integer

instance.GetEdgeInformation(EdgeCountBefore, EdgeCountAfter)
```

### C#

```csharp
void GetEdgeInformation(
   out System.int EdgeCountBefore,
   out System.int EdgeCountAfter
)
```

### C++/CLI

```cpp
void GetEdgeInformation(
   [Out] System.int EdgeCountBefore,
   [Out] System.int EdgeCountAfter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCountBefore`: Number of edges before healing
- `EdgeCountAfter`: Number of edges after healing

## VBA Syntax

See [HealEdgesFeatureData::GetEdgeInformation](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~GetEdgeInformation.html).

## Examples

[Modify Heal Edges Feature (VBA)](Modify_Heal_Edges_Feature_Example_VB.htm)
[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
