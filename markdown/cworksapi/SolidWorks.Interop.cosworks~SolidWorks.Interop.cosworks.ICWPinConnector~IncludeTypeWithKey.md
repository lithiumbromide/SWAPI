---
title: "IncludeTypeWithKey Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "IncludeTypeWithKey"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithKey.html"
---

# IncludeTypeWithKey Property (ICWPinConnector)

Gets or sets whether to prevent relative rotation between the two cylindrical faces of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeTypeWithKey As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Boolean

instance.IncludeTypeWithKey = value

value = instance.IncludeTypeWithKey
```

### C#

```csharp
System.bool IncludeTypeWithKey {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeTypeWithKey {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to prevent relative rotation between the two cylindrical faces, false to not (see **Remarks**)

## VBA Syntax

See [CWPinConnector::IncludeTypeWithKey](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~IncludeTypeWithKey.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

If this property is set to true, then:

- Do not set [ICWPinConnector::RotationalStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~RotationalStiffnessValue.html).
- Do set [ICWPinConnector::AxialStiffnessValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AxialStiffnessValue.html) only if [ICWPinConnector::IncludeTypeWithRetainerRing](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeTypeWithRetainerRing.html) is set to false.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
