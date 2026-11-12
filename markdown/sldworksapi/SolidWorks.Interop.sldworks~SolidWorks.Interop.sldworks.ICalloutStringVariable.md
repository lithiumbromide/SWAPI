---
title: "ICalloutStringVariable Interface"
project: "SOLIDWORKS API Help"
interface: "ICalloutStringVariable"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.html"
---

# ICalloutStringVariable Interface

Allows access to a string variable in a hole callout.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICalloutStringVariable
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutStringVariable
```

### C#

```csharp
public interface ICalloutStringVariable
```

### C++/CLI

```cpp
public interface class ICalloutStringVariable
```

## VBA Syntax

See [CalloutStringVariable](ms-its:sldworksapivb6.chm::/sldworks~CalloutStringVariable.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

To access a CalloutStringVariable object:

1. Call [IDisplayDimension::GetHoleCalloutVariables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.html).
2. Iterate through the [CalloutVariable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html) objects returned by IDisplayDimension::GetHoleCalloutVariables and call [ICalloutVariable::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.html).

If the type of hole callout equals [swCalloutVariableType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariableType_e.html).swCalloutVariable_String, then that object is a CalloutStringVariable object.

## Access Diagram

[CalloutStringVariable](SWObjectModel.pdf#CalloutStringVariable)

## See Also

[ICalloutStringVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html)
[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
