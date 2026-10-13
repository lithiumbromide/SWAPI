---
title: "ToleranceType Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "ToleranceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceType.html"
---

# ToleranceType Property (ICalloutVariable)

Gets or sets the type of tolerance for a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Integer

instance.ToleranceType = value

value = instance.ToleranceType
```

### C#

```csharp
System.int ToleranceType {get; set;}
```

### C++/CLI

```cpp
property System.int ToleranceType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of tolerance as defined in [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html) (see **Remarks**)

## VBA Syntax

See [CalloutVariable::ToleranceType](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~ToleranceType.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

In SOLIDWORKS 2016 and later, use this property to set the type of tolerance for a hole callout. Calling [IDimensionTolerance::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html) to set the type of tolerance for a hole callout does not override this property's setting.

To see the effects of changing the tolerance type, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
