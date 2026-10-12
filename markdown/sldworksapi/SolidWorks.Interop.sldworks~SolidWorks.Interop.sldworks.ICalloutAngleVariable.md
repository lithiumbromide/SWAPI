---
title: "ICalloutAngleVariable Interface"
project: "SOLIDWORKS API Help"
interface: "ICalloutAngleVariable"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html"
---

# ICalloutAngleVariable Interface

Allows access to an angle variable in a hole callout.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICalloutAngleVariable
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutAngleVariable
```

### C#

```csharp
public interface ICalloutAngleVariable
```

### C++/CLI

```cpp
public interface class ICalloutAngleVariable
```

## VBA Syntax

See [CalloutAngleVariable](ms-its:sldworksapivb6.chm::/sldworks~CalloutAngleVariable.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

To access a CalloutAngleVariable object:

1. Call [IDisplayDimension::GetHoleCalloutVariables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.html).
2. Iterate through the [CalloutVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html) objects returned by IDisplayDimension::GetHoleCalloutVariables and call [ICalloutVariable::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.html).

If the type of hole callout equals [swCalloutVariableType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariableType_e.html).swCalloutVariable_Angle, then that object is a CalloutAngleVariable object.

## Access Diagram

[CalloutAngleVariable](SWObjectModel.pdf#CalloutAngleVariable)

## See Also

[ICalloutAngleVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.html)
