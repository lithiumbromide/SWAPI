---
title: "InsertRecord Method (IHelixFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHelixFeatureData"
member: "InsertRecord"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord.html"
---

# InsertRecord Method (IHelixFeatureData)

Inserts a record before the specified index in the Region parameters table of this variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRecord( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.InsertRecord(Index)
```

### C#

```csharp
System.bool InsertRecord(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool InsertRecord(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index after which to insert a new record

### Return Value

True if the record is inserted, false if not

## VBA Syntax

See [HelixFeatureData::InsertRecord](ms-its:sldworksapivb6.chm::/sldworks~HelixFeatureData~InsertRecord.html).

## Remarks

When inserting a record, the SOLIDWORKS Design software calculates the new region's parameters. You cannot add a record to the beginning of the Region parameters table. To add a record to the end of the Region parameters table, use [IHelixFeatureData::AddLastRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.html).

## See Also

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html)
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.html)
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.html)
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.html)
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.html)
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
