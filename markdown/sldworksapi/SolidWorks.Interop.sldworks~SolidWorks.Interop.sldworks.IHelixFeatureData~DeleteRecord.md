---
title: "DeleteRecord Method (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "DeleteRecord"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.html"
---

# DeleteRecord Method (IHelixFeatureData)

Deletes the specified records in the Region parameters table of this variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRecord( _
   ByVal Indices As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim Indices As System.Object
Dim value As System.Boolean

value = instance.DeleteRecord(Indices)
```

### C#

```csharp
System.bool DeleteRecord(
   System.object Indices
)
```

### C++/CLI

```cpp
System.bool DeleteRecord(
   System.Object^ Indices
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Indices`: Array of the indices of the records to delete (see **Remarks**)

### Return Value

True if the records are deleted, false if not

## VBA Syntax

See [HelixFeatureData::DeleteRecord](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~DeleteRecord.html).

## Examples

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

You cannot delete the first record in the Regions parameters table.

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html)
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.html)
[IHelixFeatureData::InsertRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.html)
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.html)
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.html)
[IHelixFeatureData::AddLastRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
