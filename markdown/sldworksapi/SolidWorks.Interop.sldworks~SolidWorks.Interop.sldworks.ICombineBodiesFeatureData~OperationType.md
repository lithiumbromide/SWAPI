---
title: "OperationType Property (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "OperationType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~OperationType.html"
---

# OperationType Property (ICombineBodiesFeatureData)

Gets or sets how to combine multiple solid bodies for a combine feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OperationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim value As System.Integer

instance.OperationType = value

value = instance.OperationType
```

### C#

```csharp
System.int OperationType {get; set;}
```

### C++/CLI

```cpp
property System.int OperationType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of combination as defined in [swCombineBodiesOperationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCombineBodiesOperationType_e.html)

## VBA Syntax

See [CombineBodiesFeatureData::OperationType](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~OperationType.html).

## Examples

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
