---
title: "GetPoints Method (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "GetPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~GetPoints.html"
---

# GetPoints Method (IPrimaryMemberPointLengthFeatureData)

Gets the vertexes, sketch points, and reference points used to create this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Object

value = instance.GetPoints()
```

### C#

```csharp
System.object GetPoints()
```

### C++/CLI

```cpp
System.Object^ GetPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)es, [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)s, and/or [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)s

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::GetPoints](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~GetPoints.html).

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
