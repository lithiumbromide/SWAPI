---
title: "GetHoleCalloutVariables Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetHoleCalloutVariables"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.html"
---

# GetHoleCalloutVariables Method (IDisplayDimension)

Gets access to hole callout variables in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleCalloutVariables() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Object

value = instance.GetHoleCalloutVariables()
```

### C#

```csharp
System.object GetHoleCalloutVariables()
```

### C++/CLI

```cpp
System.Object^ GetHoleCalloutVariables();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [CalloutVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html) objects

## VBA Syntax

See [DisplayDimension::GetHoleCalloutVariables](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetHoleCalloutVariables.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html)
[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.html)
[IDisplayDimension::IsHoleCallout Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html)
[IDrawingDoc::AddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.html)
[IDrawingDoc::IAddHoleCallout2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
