---
title: "ShowParenthesis Property (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "ShowParenthesis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~ShowParenthesis.html"
---

# ShowParenthesis Property (IDimensionTolerance)

Indicates whether to show parentheses around linear tolerance dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowParenthesis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Boolean

instance.ShowParenthesis = value

value = instance.ShowParenthesis
```

### C#

```csharp
System.bool ShowParenthesis {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show parentheses around linear tolerance dimensions, false to not

## VBA Syntax

See [DimensionTolerance::ShowParenthesis](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~ShowParenthesis.html).

## Remarks

This property supports bilateral, symmetric, or fit-with-tolerance types only.

In SOLIDWORKS 2016 and later, use [ICalloutVariable::ShowParenthesis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis.html) to set whether to show parentheses in a hole's display dimension with multiple values in a callout. Calling IDimensionTolerance::ShowParenthesis to set whether to show parentheses in a hole's display dimension with multiple values in a callout does not override ICalloutVariable::ShowParenthesis' setting.

To see the effects of changing this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::ShowParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
