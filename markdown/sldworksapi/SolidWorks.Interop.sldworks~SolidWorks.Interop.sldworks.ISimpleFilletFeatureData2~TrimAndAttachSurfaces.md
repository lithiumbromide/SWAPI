---
title: "TrimAndAttachSurfaces Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "TrimAndAttachSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~TrimAndAttachSurfaces.html"
---

# TrimAndAttachSurfaces Property (ISimpleFilletFeatureData2)

Gets or sets the Trim surfaces option for surface face fillets.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimAndAttachSurfaces As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

instance.TrimAndAttachSurfaces = value

value = instance.TrimAndAttachSurfaces
```

### C#

```csharp
System.int TrimAndAttachSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.int TrimAndAttachSurfaces {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = Trim and attach (trims the filleted face and knits the surfaces into one surface body)

- 1 = Don't trim or attach (adds a new fillet surface, but does not trim the faces or knit the surfaces)

- -1 = Not applicable

## VBA Syntax

See [SimpleFilletFeatureData2::TrimAndAttachSurfaces](ms-its:sldworksapivb6.chm::/Sldworks~SimpleFilletFeatureData2~TrimAndAttachSurfaces.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
