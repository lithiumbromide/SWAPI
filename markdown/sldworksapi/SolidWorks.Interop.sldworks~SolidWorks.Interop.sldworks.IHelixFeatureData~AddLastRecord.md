---
title: "AddLastRecord Method (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "AddLastRecord"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.html"
---

# AddLastRecord Method (IHelixFeatureData)

Adds a region to the end of the Region parameters table of this variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLastRecord( _
   ByVal HelixPointValue As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim HelixPointValue As System.Object
Dim value As System.Boolean

value = instance.AddLastRecord(HelixPointValue)
```

### C#

```csharp
System.bool AddLastRecord(
   System.object HelixPointValue
)
```

### C++/CLI

```cpp
System.bool AddLastRecord(
   System.Object^ HelixPointValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HelixPointValue`: Array of four doubles for the region to add to the end of the Region parameters table (see **Remarks**)

### Return Value

True if the region is added to the end of the Region parameters table, false if not

## VBA Syntax

See [HelixFeatureData::AddLastRecord](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~AddLastRecord.html).

## Examples

[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

The values in the array specified for HelixPointValue depends on the type of variable-pitch helix:

| Helix type | Array of doubles in this order |
| --- | --- |
| Pitch and revolution | Pitch, number of revolutions, 0, diameter |
| Height and revolution | Height, number of revolutions, 0, diameter |
| Height and pitch | Height, pitch, 0, diameter |

**NOTE:** You must specify 0 for any element that SOLIDWORKS calculates.

To insert a record at a specific index in the Region parameters table (i.e., between existing records) of this variable-pitch helix, use [IHelixFeatureData::InsertRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.html)
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.html)
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.html)
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.html)
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
