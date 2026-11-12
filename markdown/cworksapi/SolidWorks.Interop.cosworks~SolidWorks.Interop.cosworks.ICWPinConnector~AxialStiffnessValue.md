---
title: "AxialStiffnessValue Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "AxialStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AxialStiffnessValue.html"
---

# AxialStiffnessValue Property (ICWPinConnector)

Gets or sets the axial stiffness of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property AxialStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.AxialStiffnessValue = value

value = instance.AxialStiffnessValue
```

### C#

```csharp
System.double AxialStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double AxialStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Axial stiffness value (see **Remarks**)

## VBA Syntax

See [CWPinConnector::AxialStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~AxialStiffnessValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWPinConnector::IncludeTypeWithRetainerRing](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithRetainerRing.html) is set to false.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::RotationalStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RotationalStiffnessValue.html)
[ICWPinConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~Unit.html)
[ICWPinConnector::IncludeTypeWithKey Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithKey.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
