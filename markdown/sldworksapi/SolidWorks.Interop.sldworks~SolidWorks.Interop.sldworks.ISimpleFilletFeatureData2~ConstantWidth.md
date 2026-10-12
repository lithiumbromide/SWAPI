---
title: "ConstantWidth Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ConstantWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConstantWidth.html"
---

# ConstantWidth Property (ISimpleFilletFeatureData2)

Gets or sets whether this simple fillet has a constant width.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConstantWidth As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.ConstantWidth = value

value = instance.ConstantWidth
```

### C#

```csharp
System.bool ConstantWidth {get; set;}
```

### C++/CLI

```cpp
property System.bool ConstantWidth {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if simple fillet has constant width, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::ConstantWidth](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~ConstantWidth.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
