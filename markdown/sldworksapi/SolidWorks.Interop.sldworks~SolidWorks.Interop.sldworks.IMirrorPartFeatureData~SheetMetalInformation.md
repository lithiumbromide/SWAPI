---
title: "SheetMetalInformation Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "SheetMetalInformation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~SheetMetalInformation.html"
---

# SheetMetalInformation Property (IMirrorPartFeatureData)

Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetMetalInformation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.SheetMetalInformation = value

value = instance.SheetMetalInformation
```

### C#

```csharp
System.bool SheetMetalInformation {get; set;}
```

### C++/CLI

```cpp
property System.bool SheetMetalInformation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part, false to not

## VBA Syntax

See [MirrorPartFeatureData::SheetMetalInformation](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~SheetMetalInformation.html).

## Examples

[Mirror Sheet-metal Part (C#)](Mirror_Sheet-metal_Part_Example_CSharp.htm)
[Mirror Sheet-metal Part (VB.NET)](Mirror_Sheet-metal_Part_Example_VBNET.htm)
[Mirror Sheet-metal Part (VBA)](Mirror_Sheet-metal_Part_Example_VB.htm)

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)
[IMirrorPartFeatureData::UnlockedProperties Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~UnlockedProperties.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
