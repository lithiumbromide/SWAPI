---
title: "DetailedCutList Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "DetailedCutList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.html"
---

# DetailedCutList Property (IBomFeature)

Gets or sets whether to show the detailed cut list in this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property DetailedCutList As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.DetailedCutList = value

value = instance.DetailedCutList
```

### C#

```csharp
System.bool DetailedCutList {get; set;}
```

### C++/CLI

```cpp
property System.bool DetailedCutList {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show the detailed cut list in the BOM table, false to not

## VBA Syntax

See [BomFeature::DetailedCutList](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~DetailedCutList.html).

## Remarks

This property applies to all types of BOM tables.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::DissolvePartLevelRows Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.html)

## Availability

SOLIDWORKS 2012 SP02, Revision Number 20.2
