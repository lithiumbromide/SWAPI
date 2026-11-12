---
title: "DimensionText Property (IPMIDimensionData)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionData"
member: "DimensionText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~DimensionText.html"
---

# DimensionText Property (IPMIDimensionData)

Gets the text of this PMI dimension.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionData
Dim value As System.String

instance.DimensionText = value

value = instance.DimensionText
```

### C#

```csharp
System.string DimensionText {get; set;}
```

### C++/CLI

```cpp
property System.String^ DimensionText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dimension text

## VBA Syntax

See [PMIDimensionData::DimensionText](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionData~DimensionText.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData.html)
[IPMIDimensionData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
