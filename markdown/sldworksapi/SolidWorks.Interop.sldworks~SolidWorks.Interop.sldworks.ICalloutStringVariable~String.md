---
title: "String Property (ICalloutStringVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutStringVariable"
member: "String"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable~String.html"
---

# String Property (ICalloutStringVariable)

Gets or sets the text for this string variable in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property String As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutStringVariable
Dim value As System.String

value = instance.String
```

### C#

```csharp
System.string String {get;}
```

### C++/CLI

```cpp
property System.String^ String {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text

## VBA Syntax

See [CalloutStringVariable::String](ms-its:sldworksapivb6.chm::/sldworks~CalloutStringVariable~String.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## See Also

[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.html)
[ICalloutStringVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
