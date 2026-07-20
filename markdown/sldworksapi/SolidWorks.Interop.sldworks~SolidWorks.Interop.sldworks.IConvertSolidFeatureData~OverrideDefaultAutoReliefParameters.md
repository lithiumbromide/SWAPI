---
title: "OverrideDefaultAutoReliefParameters Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "OverrideDefaultAutoReliefParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.html"
---

# OverrideDefaultAutoReliefParameters Property (IConvertSolidFeatureData)

Gets or sets whether to override the default sheet metal auto relief parameters such as relief type and relief ratio for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultAutoReliefParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.OverrideDefaultAutoReliefParameters = value

value = instance.OverrideDefaultAutoReliefParameters
```

### C#

```csharp
System.bool OverrideDefaultAutoReliefParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaultAutoReliefParameters {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to override the default sheet metal auto relief parameters, false to not

## VBA Syntax

See

[ConvertSolidFeatureData::OverrideDefaultAutoReliefParameters](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.html)

.

## Remarks

If this property is set to true, you can set:

- [IConvertSolidFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefRatio.html)
- [IConvertSolidFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefType.html)

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
