---
title: "GetFastenerTableTypes Method (IHoleStandardsData)"
project: "SOLIDWORKS API Help"
interface: "IHoleStandardsData"
member: "GetFastenerTableTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes.html"
---

# GetFastenerTableTypes Method (IHoleStandardsData)

Gets the array of three fastener table type IDs for the given fastener in the given Hole Wizard standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFastenerTableTypes( _
   ByVal StandardName As System.String, _
   ByVal FastenerID As System.Integer, _
   ByRef FastenerTableTypeIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerID As System.Integer
Dim FastenerTableTypeIDs As System.Object
Dim value As System.Boolean

value = instance.GetFastenerTableTypes(StandardName, FastenerID, FastenerTableTypeIDs)
```

### C#

```csharp
System.bool GetFastenerTableTypes(
   System.string StandardName,
   System.int FastenerID,
   out System.object FastenerTableTypeIDs
)
```

### C++/CLI

```cpp
System.bool GetFastenerTableTypes(
   System.String^ StandardName,
   System.int FastenerID,
   [Out] System.Object^ FastenerTableTypeIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StandardName`: Standard name (see **Remarks**)
- `FastenerID`: Fastener ID (see **Remarks**)
- `FastenerTableTypeIDs`: Array of three fastener table type IDs (see **Remarks**)

### Return Value

True if the fastener table type IDs are successfully retrieved, false if not

## VBA Syntax

See [HoleStandardsData::GetFastenerTableTypes](ms-its:sldworksapivb6.chm::/sldworks~HoleStandardsData~GetFastenerTableTypes.html).

## Examples

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html) example.

## Remarks

Each fastener in a given standard has three tables associated with it: size, thread data, and screw clearances. This method retrieves internal IDs of all three table types as defined in [swFastenerTableTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFastenerTableTypes_e.html) for FastenerID in StandardName.

To set:

- StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.html).
- FastenerID, use [IHoleStandardsData::GetFastenerTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.html).

## See Also

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html)
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
