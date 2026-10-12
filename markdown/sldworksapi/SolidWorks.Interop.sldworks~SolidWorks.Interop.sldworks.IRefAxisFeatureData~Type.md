---
title: "Type Property (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~Type.html"
---

# Type Property (IRefAxisFeatureData)

Gets or sets the type of reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of reference axis feature as defined by [swRefAxisType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefAxisType_e.html)

## VBA Syntax

See [RefAxisFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~RefAxisFeatureData~Type.html).

## Examples

[Get Reference Axis Data (VBA)](Get_Reference_Axis_Data_Example_VB.htm)
[Get Reference Axis Data (VB.NET)](Get_Reference_Axis_Data_Example_VBNET.htm)
[Get Reference Axis Data (C#)](Get_Reference_Axis_Data_Example_CSharp.htm)

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
