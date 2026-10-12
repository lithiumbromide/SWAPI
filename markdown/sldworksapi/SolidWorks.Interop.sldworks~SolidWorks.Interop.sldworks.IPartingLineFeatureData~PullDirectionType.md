---
title: "PullDirectionType Property (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "PullDirectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.html"
---

# PullDirectionType Property (IPartingLineFeatureData)

Gets the type of entity indicating the direction of pull.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PullDirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim value As System.Integer

value = instance.PullDirectionType
```

### C#

```csharp
System.int PullDirectionType {get;}
```

### C++/CLI

```cpp
property System.int PullDirectionType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of entity indicating the direction of pull as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelEDGES
- swSelFACES
- swSelDATUMAXES
- swSelDATUMPLANES

## VBA Syntax

See [PartingLineFeatureData::PullDirectionType](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~PullDirectionType.html).

## Examples

[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html)
[IPartingLineFeatureData::PullDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.html)
[IPartingLineFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
