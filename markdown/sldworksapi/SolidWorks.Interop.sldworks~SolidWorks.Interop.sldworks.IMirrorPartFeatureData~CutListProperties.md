---
title: "CutListProperties Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "CutListProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CutListProperties.html"
---

# CutListProperties Property (IMirrorPartFeatureData)

Gets or sets whether to import cut-list properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutListProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.CutListProperties = value

value = instance.CutListProperties
```

### C#

```csharp
System.bool CutListProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool CutListProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import cut-list properties, false to not

## VBA Syntax

See [MirrorPartFeatureData::CutListProperties](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~CutListProperties.html).

## Examples

[Mirror Sheet-metal Part (C#)](Mirror_Sheet-metal_Part_Example_CSharp.htm)
[Mirror Sheet-metal Part (VB.NET)](Mirror_Sheet-metal_Part_Example_VBNET.htm)
[Mirror Sheet-metal Part (VBA)](Mirror_Sheet-metal_Part_Example_VB.htm)

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)
[IMirrorPartFeatureData::UnlockedProperties Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnlockedProperties.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
