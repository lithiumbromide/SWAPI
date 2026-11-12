---
title: "Angle Property (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Angle.html"
---

# Angle Property (IPartingLineFeatureData)

Gets or sets the draft angle for the parting line.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Draft angle in radians

## VBA Syntax

See [PartingLineFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~Angle.html).

## Examples

[Set Options for Parting Line (VBA)](Set_Split_Faces_Option_for_Parting_Line_Example_VB.htm)
[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
