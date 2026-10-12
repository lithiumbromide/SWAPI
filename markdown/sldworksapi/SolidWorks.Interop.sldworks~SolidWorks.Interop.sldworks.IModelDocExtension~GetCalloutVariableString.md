---
title: "GetCalloutVariableString Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCalloutVariableString"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCalloutVariableString.html"
---

# GetCalloutVariableString Method (IModelDocExtension)

Gets the string for the specified callout variable.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCalloutVariableString( _
   ByVal Variable As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Variable As System.Integer
Dim value As System.String

value = instance.GetCalloutVariableString(Variable)
```

### C#

```csharp
System.string GetCalloutVariableString(
   System.int Variable
)
```

### C++/CLI

```cpp
System.String^ GetCalloutVariableString(
   System.int Variable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Variable`: Callout variable as defined in [swCalloutVariable_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html)

### Return Value

Callout variable string

## VBA Syntax

See [ModelDocExtension::GetCalloutVariableString](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCalloutVariableString.html).

## Examples

[Create Advanced Hole (VBA)](Create_Advanced_Hole_Example_VB.htm)
[Create Advanced Hole (VB.NET)](Create_Advanced_Hole_Example_VBNET.htm)
[Create Advanced Hole (C#)](Create_Advanced_Hole_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IAdvancedHoleElementData::CalloutString Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
