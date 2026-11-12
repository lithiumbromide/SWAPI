---
title: "FromToReverse Property (ICosmeticWeldBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticWeldBeadFeatureData"
member: "FromToReverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToReverse.html"
---

# FromToReverse Property (ICosmeticWeldBeadFeatureData)

Gets or sets whether to start the weld from the opposite end.

## Syntax

### Visual Basic (Declaration)

```vb
Property FromToReverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Boolean

instance.FromToReverse = value

value = instance.FromToReverse
```

### C#

```csharp
System.bool FromToReverse {get; set;}
```

### C++/CLI

```cpp
property System.bool FromToReverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the weld starts at the end opposite to [ICosmeticWeldBeadFeatureData::FromToStartPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.html), false if not (see **Remarks**)

## VBA Syntax

See [CosmeticWeldBeadFeatureData::FromToReverse](ms-its:sldworksapivb6.chm::/sldworks~CosmeticWeldBeadFeatureData~FromToReverse.html).

## Examples

See [ICosmeticWeldBeadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData.html) examples.

## Remarks

This property is valid only if [ICosmeticWeldBeadFeatureData::FromToLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToLength.html) is true.

## See Also

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.html)
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html)
[ICosmeticWeldBeadFeatureData::FromToStartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToStartPoint.html)
[ICosmeticWeldBeadFeatureData::FromToWeldLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~FromToWeldLength.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
