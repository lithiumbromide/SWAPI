---
title: "DissolvePartLevelRows Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "DissolvePartLevelRows"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.html"
---

# DissolvePartLevelRows Property (IBomFeature)

Gets or sets whether to dissolve weldment part level rows.

## Syntax

### Visual Basic (Declaration)

```vb
Property DissolvePartLevelRows As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.DissolvePartLevelRows = value

value = instance.DissolvePartLevelRows
```

### C#

```csharp
System.bool DissolvePartLevelRows {get; set;}
```

### C++/CLI

```cpp
property System.bool DissolvePartLevelRows {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to dissolve component rows, false to not

## VBA Syntax

See [BomFeature::DissolvePartLevelRows](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~DissolvePartLevelRows.html).

## Remarks

This getter of this property is valid only when [IBomFeature::DetailedCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.html) is set to true.

The setter of this property is valid only for:

- BOM tables of type [swBomType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html).swBomType_Indented (call [IBomFeature::TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.html) to get the BOM table type)

- and -

- when IBomFeature::DetailedCutList is set to true.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
