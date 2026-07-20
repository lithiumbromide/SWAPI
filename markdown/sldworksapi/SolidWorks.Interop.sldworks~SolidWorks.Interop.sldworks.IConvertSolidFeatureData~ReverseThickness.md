---
title: "ReverseThickness Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "ReverseThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReverseThickness.html"
---

# ReverseThickness Property (IConvertSolidFeatureData)

Gets or sets whether to reverse the thickness direction of this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.ReverseThickness = value

value = instance.ReverseThickness
```

### C#

```csharp
System.bool ReverseThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseThickness {
   System.bool get();
   void set (    System.bool value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

True to reverse thickness direction, false to not

## VBA Syntax

See

[ConvertSolidFeatureData::ReverseThickness](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~ReverseThickness.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
