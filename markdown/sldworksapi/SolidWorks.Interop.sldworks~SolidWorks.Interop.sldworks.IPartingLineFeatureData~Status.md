---
title: "Status Method (IPartingLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingLineFeatureData"
member: "Status"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Status.html"
---

# Status Method (IPartingLineFeatureData)

Gets the status of this parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function Status() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingLineFeatureData
Dim value As System.Integer

value = instance.Status()
```

### C#

```csharp
System.int Status()
```

### C++/CLI

```cpp
System.int Status();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Status of parting line feature as defined in [swPartingLineFeatureStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingLineFeatureStatus_e.html)

## VBA Syntax

See [PartingLineFeatureData::Status](ms-its:sldworksapivb6.chm::/sldworks~PartingLineFeatureData~Status.html).

## Examples

[Get and Set Parting Line Feature Data (C#)](Get_and_Set_Parting_Line_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Line Feature Data (VB.NET)](Get_and_Set_Parting_Line_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Line Feature Data (VBA)](Get_and_Set_Parting_Line_Feature_Data_Example_VB.htm)

## Remarks

Call this method after specifying the settings and options for this feature to find out the status of the feature.

## See Also

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
