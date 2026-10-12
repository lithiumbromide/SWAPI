---
title: "GetType Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetType.html"
---

# GetType Method (ISplitLineFeatureData)

Gets the type of split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
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

Type of split line feature as defined in [swSplitLineFeatureType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html)

## VBA Syntax

See [SplitLineFeatureData::GetType](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~GetType.html).

## Examples

[Get Type of Split Line (VBA)](Get_Type_of_Split_Line_Example_VB.htm)
[Get Type of Split Line (VB.NET)](Get_Type_of_Split_Line_Example_VBNET.htm)
[Get Type of Split Line (C#)](Get_Type_of_Split_Line_Example_CSharp.htm)

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::SplitType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
