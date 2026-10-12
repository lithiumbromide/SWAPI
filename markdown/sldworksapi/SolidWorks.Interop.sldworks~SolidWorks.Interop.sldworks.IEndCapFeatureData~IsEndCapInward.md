---
title: "IsEndCapInward Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "IsEndCapInward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~IsEndCapInward.html"
---

# IsEndCapInward Property (IEndCapFeatureData)

Gets or sets the thickness direction of this end cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsEndCapInward As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Integer

instance.IsEndCapInward = value

value = instance.IsEndCapInward
```

### C#

```csharp
System.int IsEndCapInward {get; set;}
```

### C++/CLI

```cpp
property System.int IsEndCapInward {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thickness direction as defined by [swEndCapThicknessDirection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndCapThicknessDirection_e.html)

## VBA Syntax

See [EndCapFeatureData::IsEndCapInward](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~IsEndCapInward.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
