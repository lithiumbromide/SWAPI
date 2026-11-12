---
title: "GetHoleStandards Method (IHoleStandardsData)"
project: "SOLIDWORKS API Help"
interface: "IHoleStandardsData"
member: "GetHoleStandards"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.html"
---

# GetHoleStandards Method (IHoleStandardsData)

Gets Hole Wizard standards.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleStandards( _
   ByRef Indexes As System.Object, _
   ByRef Names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleStandardsData
Dim Indexes As System.Object
Dim Names As System.Object
Dim value As System.Boolean

value = instance.GetHoleStandards(Indexes, Names)
```

### C#

```csharp
System.bool GetHoleStandards(
   out System.object Indexes,
   out System.object Names
)
```

### C++/CLI

```cpp
System.bool GetHoleStandards(
   [Out] System.Object^ Indexes,
   [Out] System.Object^ Names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Indexes`: Array of Hole Wizard standards as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandards_e.html)
- `Names`: Array of names of Hole Wizard standards

### Return Value

True if Hole Wizard standards retrieved successfully, false if not

## VBA Syntax

See [HoleStandardsData::GetHoleStandards](ms-its:sldworksapivb6.chm::/sldworks~HoleStandardsData~GetHoleStandards.html).

## Examples

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html) example.

## See Also

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html)
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.html)
[IHoleStandardsData::GetFastenerTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTable.html)
[IHoleStandardsData::GetFastenerTableTypes Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes.html)
[IHoleStandardsData::GetFastenerTypes Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
