---
title: "GetPointsTypes Method (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "GetPointsTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~GetPointsTypes.html"
---

# GetPointsTypes Method (IPrimaryMemberPointLengthFeatureData)

Gets the types of points.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPointsTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Object

value = instance.GetPointsTypes()
```

### C#

```csharp
System.object GetPointsTypes()
```

### C++/CLI

```cpp
System.Object^ GetPointsTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of point types as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelSKETCHPOINTS
- swSelEXTSKETCHPOINTS
- swSelVERTICES

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::GetPointsTypes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~GetPointsTypes.html).

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
