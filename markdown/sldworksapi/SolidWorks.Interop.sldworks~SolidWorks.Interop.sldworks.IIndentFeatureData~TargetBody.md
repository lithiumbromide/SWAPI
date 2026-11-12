---
title: "TargetBody Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "TargetBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html"
---

# TargetBody Property (IIndentFeatureData)

Gets or sets the solid or surface body to indent.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetBody As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Object

instance.TargetBody = value

value = instance.TargetBody
```

### C#

```csharp
System.object TargetBody {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TargetBody {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Solid or surface [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html) to indent

## VBA Syntax

See [IndentFeatureData::TargetBody](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~TargetBody.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)
[IIndentFeatureData::IsCut Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.html)
[IIndentFeatureData::SelectionState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~SelectionState.html)
[IIndentFeatureData::ToolBodyRegion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
