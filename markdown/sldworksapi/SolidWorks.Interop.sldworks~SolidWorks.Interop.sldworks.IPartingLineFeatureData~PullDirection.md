---
title: "PullDirection Property (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "PullDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.html"
---

# PullDirection Property (IPartingLineFeatureData)

Gets whether the direction of pull is reversed.

## Syntax

### Visual Basic (Declaration)

```vb
Property PullDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim value As System.Boolean

instance.PullDirection = value

value = instance.PullDirection
```

### C#

```csharp
System.bool PullDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool PullDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the direction of pull is reversed, false if not

## VBA Syntax

See [PartingLineFeatureData::PullDirection](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~PullDirection.html).

## Examples

[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.html)
[IPartingLineFeatureData::PullDirectionBase Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.html)
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
