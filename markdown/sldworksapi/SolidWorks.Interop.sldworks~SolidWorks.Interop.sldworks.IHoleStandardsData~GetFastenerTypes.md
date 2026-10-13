---
title: "GetFastenerTypes Method (IHoleStandardsData)"
project: "SOLIDWORKS API Help"
interface: "IHoleStandardsData"
member: "GetFastenerTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.html"
---

# GetFastenerTypes Method (IHoleStandardsData)

Gets the fasteners in the specified Hole Wizard standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFastenerTypes( _
   ByVal StandardName As System.String, _
   ByRef FastenerIndexes As System.Object, _
   ByRef FastenerNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerIndexes As System.Object
Dim FastenerNames As System.Object
Dim value As System.Boolean

value = instance.GetFastenerTypes(StandardName, FastenerIndexes, FastenerNames)
```

### C#

```csharp
System.bool GetFastenerTypes(
   System.string StandardName,
   out System.object FastenerIndexes,
   out System.object FastenerNames
)
```

### C++/CLI

```cpp
System.bool GetFastenerTypes(
   System.String^ StandardName,
   [Out] System.Object^ FastenerIndexes,
   [Out] System.Object^ FastenerNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StandardName`: Standard name (see **Remarks**)
- `FastenerIndexes`: Array of fastener indexes
- `FastenerNames`: Array of fastener names

### Return Value

True if fastener types successfully retrieved, false if not

## VBA Syntax

See [HoleStandardsData::GetFastenerTypes](ms-its:sldworksapivb6.chm::/sldworks~HoleStandardsData~GetFastenerTypes.html).

## Examples

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html) example.

## Remarks

To set StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.html).

## See Also

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.html)
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
