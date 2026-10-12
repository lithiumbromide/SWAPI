---
title: "GetBodiesCount Method (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "GetBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~GetBodiesCount.html"
---

# GetBodiesCount Method (IIndentFeatureData)

Gets the number of solid or surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) for the [tool body region](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Integer

value = instance.GetBodiesCount()
```

### C#

```csharp
System.int GetBodiesCount()
```

### C++/CLI

```cpp
System.int GetBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solid or surface bodies for the tool body region

## VBA Syntax

See [IndentFeatureData::GetBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~GetBodiesCount.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
