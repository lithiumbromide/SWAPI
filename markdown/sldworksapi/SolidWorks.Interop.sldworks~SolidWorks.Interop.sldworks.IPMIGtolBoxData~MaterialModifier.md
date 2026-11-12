---
title: "MaterialModifier Property (IPMIGtolBoxData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolBoxData"
member: "MaterialModifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~MaterialModifier.html"
---

# MaterialModifier Property (IPMIGtolBoxData)

Gets the material condition for this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialModifier As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolBoxData
Dim value As System.Integer

instance.MaterialModifier = value

value = instance.MaterialModifier
```

### C#

```csharp
System.int MaterialModifier {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialModifier {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Material condition as defined in [swMaterialModifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html) (see Remarks)

## VBA Syntax

See [PMIGtolBoxData::MaterialModifier](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolBoxData~MaterialModifier.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

All material conditions in swMaterialModifier_e are valid except swMaterialModifier_e.swMaterialModifier_Translation.

## See Also

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.html)
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html)
[IPMIGtolBoxData::GetAdditionalSymbols Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetAdditionalSymbols.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
