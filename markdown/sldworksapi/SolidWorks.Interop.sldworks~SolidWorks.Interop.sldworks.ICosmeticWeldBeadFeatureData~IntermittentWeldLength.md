---
title: "IntermittentWeldLength Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "IntermittentWeldLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeldLength.html"
---

# IntermittentWeldLength Property (ICosmeticWeldBeadFeatureData)

Gets or sets the length of the weld for intermittent weld beads.

## Syntax

### Visual Basic (Declaration)

```vb
Property IntermittentWeldLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Double

instance.IntermittentWeldLength = value

value = instance.IntermittentWeldLength
```

### C#

```csharp
System.double IntermittentWeldLength {get; set;}
```

### C++/CLI

```cpp
property System.double IntermittentWeldLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of weld for intermittent weld beads (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::IntermittentWeldLength](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~IntermittentWeldLength.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::IntermittentWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~IntermittentWeld.html) is true.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
