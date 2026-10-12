---
title: "GetFastenerTable Method (IHoleStandardsData)"
project: "SOLIDWORKS API Help"
interface: "IHoleStandardsData"
member: "GetFastenerTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTable.html"
---

# GetFastenerTable Method (IHoleStandardsData)

Gets the Hole Wizard fastener table for the specified Hole Wizard standard, fastener ID, and fastener table type ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFastenerTable( _
   ByVal StandardName As System.String, _
   ByVal FastenerID As System.Integer, _
   ByVal TableID As System.Integer, _
   ByRef HoleTable As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerID As System.Integer
Dim TableID As System.Integer
Dim HoleTable As System.Object
Dim value As System.Boolean

value = instance.GetFastenerTable(StandardName, FastenerID, TableID, HoleTable)
```

### C#

```csharp
System.bool GetFastenerTable(
   System.string StandardName,
   System.int FastenerID,
   System.int TableID,
   out System.object HoleTable
)
```

### C++/CLI

```cpp
System.bool GetFastenerTable(
   System.String^ StandardName,
   System.int FastenerID,
   System.int TableID,
   [Out] System.Object^ HoleTable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StandardName`: Standard name (see **Remarks**)
- `FastenerID`: Fastener ID (see **Remarks**)
- `TableID`: Fastener table type ID (see **Remarks**)
- `HoleTable`: [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.html)

### Return Value

True if fastener data table successfully retrieved, false if not

## VBA Syntax

See [HoleStandardsData::GetFastenerTable](ms-its:sldworksapivb6.chm::/sldworks~HoleStandardsData~GetFastenerTable.html).

## Examples

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html) example.

## Remarks

To set:

- StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.html).
- FastenerID, use [IHoleStandardsData::GetFastenerTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.html).
- TableID, use [IHoleStandardsData::GetFastenerTableTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes.html).

## See Also

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html)
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
