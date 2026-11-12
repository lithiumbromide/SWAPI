---
title: "UseTextScale Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "UseTextScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.html"
---

# UseTextScale Property (ICalloutVariable)

Gets or sets whether to use the value with which to scale the tolerance text for a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTextScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Boolean

instance.UseTextScale = value

value = instance.UseTextScale
```

### C#

```csharp
System.bool UseTextScale {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTextScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the value with which to scale the tolerance text, false to not

## VBA Syntax

See [CalloutVariable::UseTextScale](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~UseTextScale.html).

## Remarks

Call [ICalloutVariable::TextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.html) to get or set the value with which to scale the tolerance text.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
