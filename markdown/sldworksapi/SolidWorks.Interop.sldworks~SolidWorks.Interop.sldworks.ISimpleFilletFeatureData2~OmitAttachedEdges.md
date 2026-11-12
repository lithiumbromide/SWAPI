---
title: "OmitAttachedEdges Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "OmitAttachedEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~OmitAttachedEdges.html"
---

# OmitAttachedEdges Property (ISimpleFilletFeatureData2)

Gets whether the simple fillet feature is not applied to the attachment edges of the feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OmitAttachedEdges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.OmitAttachedEdges = value

value = instance.OmitAttachedEdges
```

### C#

```csharp
System.bool OmitAttachedEdges {get; set;}
```

### C++/CLI

```cpp
property System.bool OmitAttachedEdges {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if fillet is not applied to the attachment edges, false if it is

## VBA Syntax

See [SimpleFilletFeatureData2::OmitAttachedEdges](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~OmitAttachedEdges.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
