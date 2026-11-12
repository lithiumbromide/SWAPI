---
title: "GetReferencePointType Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetReferencePointType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetReferencePointType.html"
---

# GetReferencePointType Method (ITablePatternFeatureData)

Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencePointType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetReferencePointType()
```

### C#

```csharp
System.int GetReferencePointType()
```

### C++/CLI

```cpp
System.int GetReferencePointType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of reference point:

- 0 = closed curve
- 1 = sketch point
- 2 = vertex

## VBA Syntax

See [TablePatternFeatureData::GetReferencePointType](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetReferencePointType.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::ReferencePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ReferencePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
