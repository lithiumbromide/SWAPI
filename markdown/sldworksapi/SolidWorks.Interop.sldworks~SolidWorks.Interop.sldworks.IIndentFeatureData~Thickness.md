---
title: "Thickness Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Thickness.html"
---

# Thickness Property (IIndentFeatureData)

Gets or sets the thickness of the indent feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Double

instance.Thickness = value

value = instance.Thickness
```

### C#

```csharp
System.double Thickness {get; set;}
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thickness

## VBA Syntax

See [IndentFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~Thickness.html).

## Examples

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

## Remarks

This property applies to solid bodies only.

If [IIndentFeatureData::IsCut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.html) is set to true (i.e., remove the intersection area of the target body), then there is no thickness.

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
