---
title: "GetType Method (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetType.html"
---

# GetType Method (IOneBendFeatureData)

Gets the type of bend for this one bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Bend type as defined in [swBendType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendType_e.html)

## VBA Syntax

See [OneBendFeatureData::GetType](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~GetType.html).

## Examples

[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Names of Sketch Segments (VB.NET)](Get_Names_of_Sketch_Segments_Example_VBNET.htm)
[Get Names of Sketch Segments (C#)](Get_Names_of_Sketch_Segments_Example_CSharp.htm)

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
