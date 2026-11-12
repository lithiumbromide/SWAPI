---
title: "GetPatternFaceCount Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetPatternFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFaceCount.html"
---

# GetPatternFaceCount Method (ITablePatternFeatureData)

Gets the number of patterned faces in this table-driven feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetPatternFaceCount()
```

### C#

```csharp
System.int GetPatternFaceCount()
```

### C++/CLI

```cpp
System.int GetPatternFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of patterned faces in this table-driven feature

## VBA Syntax

See [TablePatternFeatureData::GetPatternFaceCount](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetPatternFaceCount.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFaceArray.html)
[ITablePatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFaceArray.html)
[ITablePatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
