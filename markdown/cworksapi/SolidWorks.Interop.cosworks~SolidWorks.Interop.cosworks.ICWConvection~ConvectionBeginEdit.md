---
title: "ConvectionBeginEdit Method (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "ConvectionBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~ConvectionBeginEdit.html"
---

# ConvectionBeginEdit Method (ICWConvection)

Starts editing convection.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ConvectionBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection

instance.ConvectionBeginEdit()
```

### C#

```csharp
void ConvectionBeginEdit()
```

### C++/CLI

```cpp
void ConvectionBeginEdit();
```

## VBA Syntax

See [CWConvection::ConvectionBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWConvection~ConvectionBeginEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power with Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power with Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

To start editing convection, you must call this method. You must call [ICWConvection::ConvectionEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWConvection~ConvectionEndEdit.html) to end editing that convection. Changes are not applied unless you call both methods.

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
