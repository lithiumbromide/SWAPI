---
title: "ModelDimensions Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "ModelDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~ModelDimensions.html"
---

# ModelDimensions Property (IMirrorPartFeatureData)

Gets or sets whether to import model dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Property ModelDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.ModelDimensions = value

value = instance.ModelDimensions
```

### C#

```csharp
System.bool ModelDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool ModelDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import model dimensions, false to not

## VBA Syntax

See [MirrorPartFeatureData::ModelDimensions](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~ModelDimensions.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
