---
title: "ConvectionEndEdit Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "ConvectionEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~ConvectionEndEdit.html"
---

# ConvectionEndEdit Method (ICWConvection)

Ends the editing convection.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvectionEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Integer

value = instance.ConvectionEndEdit()
```

### C#

```csharp
System.int ConvectionEndEdit()
```

### C++/CLI

```cpp
System.int ConvectionEndEdit();
```

### Return Value

Error as defined in [swsConvectionEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsConvectionEndEditError_e.html)

## VBA Syntax

See [CWConvection::ConvectionEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~ConvectionEndEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power with Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

You must call [ICWConvection::ConvectionBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWConvection~ConvectionBeginEdit.html) to start editing convection. To end editing convection, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
