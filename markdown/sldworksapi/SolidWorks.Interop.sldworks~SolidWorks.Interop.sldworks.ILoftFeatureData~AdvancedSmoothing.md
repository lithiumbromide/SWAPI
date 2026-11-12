---
title: "AdvancedSmoothing Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "AdvancedSmoothing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~AdvancedSmoothing.html"
---

# AdvancedSmoothing Property (ILoftFeatureData)

Gets or sets whether to enable advanced smoothing for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AdvancedSmoothing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

instance.AdvancedSmoothing = value

value = instance.AdvancedSmoothing
```

### C#

```csharp
System.bool AdvancedSmoothing {get; set;}
```

### C++/CLI

```cpp
property System.bool AdvancedSmoothing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables advanced smoothing, false disables it

## VBA Syntax

See [LoftFeatureData::AdvancedSmoothing](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~AdvancedSmoothing.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
