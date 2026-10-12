---
title: "ToolBodyRegion Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "ToolBodyRegion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.html"
---

# ToolBodyRegion Property (IIndentFeatureData)

Gets or sets the tool body region for the indent feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToolBodyRegion As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Object

instance.ToolBodyRegion = value

value = instance.ToolBodyRegion
```

### C#

```csharp
System.object ToolBodyRegion {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ToolBodyRegion {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tool body region, which can be an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)

## VBA Syntax

See [IndentFeatureData::ToolBodyRegion](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~ToolBodyRegion.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)
[IIndentFeatureData::GetBodiesCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~GetBodiesCount.html)
[IIndentFeatureData::TargetBody Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
