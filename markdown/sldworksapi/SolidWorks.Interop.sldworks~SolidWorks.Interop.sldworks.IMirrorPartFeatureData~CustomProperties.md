---
title: "CustomProperties Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "CustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CustomProperties.html"
---

# CustomProperties Property (IMirrorPartFeatureData)

Gets or sets whether to import custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.CustomProperties = value

value = instance.CustomProperties
```

### C#

```csharp
System.bool CustomProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool CustomProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import custom properties, false to not

## VBA Syntax

See [MirrorPartFeatureData::CustomProperties](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~CustomProperties.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
