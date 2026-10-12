---
title: "UnlockedProperties Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "UnlockedProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnlockedProperties.html"
---

# UnlockedProperties Property (IMirrorPartFeatureData)

Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnlockedProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.UnlockedProperties = value

value = instance.UnlockedProperties
```

### C#

```csharp
System.bool UnlockedProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool UnlockedProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable editing of the sheet-metal definition in this mirrored sheet-metal part, false to not

## VBA Syntax

See [MirrorPartFeatureData::UnlockedProperties](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~UnlockedProperties.html).

## Examples

[Mirror Sheet-metal Part (C#)](Mirror_Sheet-metal_Part_Example_CSharp.htm)
[Mirror Sheet-metal Part (VB.NET)](Mirror_Sheet-metal_Part_Example_VBNET.htm)
[Mirror Sheet-metal Part (VBA)](Mirror_Sheet-metal_Part_Example_VB.htm)

## Remarks

[IMirrorPartFeatureData::SheetMetalInformation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SheetMetalInformation.html) must be true to access the sheet-metal definition of the mirrored sheet-metal part. Editing the sheet-metal definition updates [cut-list properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CutListProperties.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
