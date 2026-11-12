---
title: "ShowParenthesis Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "ShowParenthesis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShowParenthesis.html"
---

# ShowParenthesis Property (ICalloutVariable)

Gets or sets whether to show parentheses around linear tolerance dimensions in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowParenthesis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
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

See [CalloutVariable::ShowParenthesis](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~ShowParenthesis.html).

## Remarks

This property supports bilateral, symmetric, or fit-with-tolerance types only.

In SOLIDWORKS 2016 and later, use this property to set whether to show parentheses around linear tolerance dimensions in a hole callout. Calling [IDimensionTolerance::ShowParenthesis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~ShowParenthesis.html) to set whether to show parentheses around linear tolerance dimensions in a hole callout does not override this property's setting.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
