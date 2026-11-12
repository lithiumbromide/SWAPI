---
title: "KeepCurrentItemNumbers Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "KeepCurrentItemNumbers"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepCurrentItemNumbers.html"
---

# KeepCurrentItemNumbers Property (IBomFeature)

Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepCurrentItemNumbers As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.KeepCurrentItemNumbers = value

value = instance.KeepCurrentItemNumbers
```

### C#

```csharp
System.bool KeepCurrentItemNumbers {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepCurrentItemNumbers {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if item numbers are kept with their components when reordering rows, false if not

## VBA Syntax

See [BomFeature::KeepCurrentItemNumbers](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~KeepCurrentItemNumbers.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## Remarks

Rows in a BOM table can be reordered in several different ways. For example, you can interactively reorder the rows manually in the Bill of Materials Properties dialog box and you can programmatically reorder rows using [IBomFeature::FollowAssemblyOrder2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2004 SP2, Revision Number 12
