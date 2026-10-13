---
title: "IncludeTypeWithRetainerRing Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "IncludeTypeWithRetainerRing"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithRetainerRing.html"
---

# IncludeTypeWithRetainerRing Property (ICWPinConnector)

Gets or sets whether to prevent relative axial translation between the two cylindrical faces of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeTypeWithRetainerRing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Boolean

instance.IncludeTypeWithRetainerRing = value

value = instance.IncludeTypeWithRetainerRing
```

### C#

```csharp
System.bool IncludeTypeWithRetainerRing {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeTypeWithRetainerRing {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to prevent relative axial translation between the two cylindrical faces, false to not (see **Remarks**)

## VBA Syntax

See [CWPinConnector::IncludeTypeWithRetainerRing](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~IncludeTypeWithRetainerRing.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

If this property is set to true, then:

- Do not set [ICWPinConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AxialStiffnessValue.html).
- Do set [ICWPinConnector::RotationalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RotationalStiffnessValue.html) only if [ICWPinConnector::IncludeTypeWithKey](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithKey.html) is set to false.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
