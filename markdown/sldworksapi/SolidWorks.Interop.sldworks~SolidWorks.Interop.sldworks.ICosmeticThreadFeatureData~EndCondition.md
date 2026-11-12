---
title: "EndCondition Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~EndCondition.html"
---

# EndCondition Property (ICosmeticThreadFeatureData)

Gets or sets the thread end condition.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer

instance.EndCondition = value

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread end condition as defined in [swCosmeticEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticEndConditions_e.html)

## VBA Syntax

See [CosmeticThreadFeatureData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~EndCondition.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
