---
title: "RotationalStiffnessValue Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "RotationalStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RotationalStiffnessValue.html"
---

# RotationalStiffnessValue Property (ICWPinConnector)

Gets or sets the rotational stiffness of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationalStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.RotationalStiffnessValue = value

value = instance.RotationalStiffnessValue
```

### C#

```csharp
System.double RotationalStiffnessValue {get; set;}
```

### C++/CLI

```cpp
property System.double RotationalStiffnessValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Rotational stiffness value

## VBA Syntax

See [CWPinConnector::RotationalStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~RotationalStiffnessValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWPinConnector::IncludeTypeWithKey](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithKey.html) is set to false.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~Unit.html)
[ICWPinConnector::AxialStiffnessValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AxialStiffnessValue.html)
[ICWPinConnector::IncludeTypeWithRetainerRing Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithRetainerRing.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
