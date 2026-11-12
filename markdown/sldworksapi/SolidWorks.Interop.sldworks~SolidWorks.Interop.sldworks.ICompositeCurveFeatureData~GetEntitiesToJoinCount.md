---
title: "GetEntitiesToJoinCount Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "GetEntitiesToJoinCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount.html"
---

# GetEntitiesToJoinCount Method (ICompositeCurveFeatureData)

Gets the number of entities that are joined to create a composite curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesToJoinCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData
Dim value As System.Integer

value = instance.GetEntitiesToJoinCount()
```

### C#

```csharp
System.int GetEntitiesToJoinCount()
```

### C++/CLI

```cpp
System.int GetEntitiesToJoinCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities

## VBA Syntax

See [CompositeCurveFeatureData::GetEntitiesToJoinCount](ms-its:sldworksapivb6.chm::/sldworks~CompositeCurveFeatureData~GetEntitiesToJoinCount.html).

## Examples

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

## Remarks

Call this method before calling [ICompositeCurveFeatureData::IGetEntitiesToJoin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin.html).

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)
[ICompositeCurveFeatureData::GetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
