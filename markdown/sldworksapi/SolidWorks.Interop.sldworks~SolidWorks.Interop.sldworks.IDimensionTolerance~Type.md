---
title: "Type Property (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html"
---

# Type Property (IDimensionTolerance)

Gets or sets the type of tolerance.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of tolerance as defined in [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html) (see **Remarks**)

## VBA Syntax

See [DimensionTolerance::Type](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~Type.html).

## Examples

See [IDimensionTolerance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance.html) examples.

## Remarks

In SOLIDWORKS 2016 and later, use [ICalloutVariable::ToleranceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType.html) to set the type of tolerance for a hole's display dimension with multiple values in a callout. Calling IDimensionTolerance::Type to set the type of tolerance for a hole's display dimension with multiple values in a callout does not override ICalloutVariable::ToleranceType's setting.

To see the effects of changing the tolerance type, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
