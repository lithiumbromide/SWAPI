---
title: "ResponseBType Property (IMessageBarDefinition)"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: "ResponseBType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition~ResponseBType.html"
---

# ResponseBType Property (IMessageBarDefinition)

Gets or sets the second response user control for this message bar.

## Syntax

### Visual Basic (Declaration)

```vb
Property ResponseBType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
Dim value As System.Integer

instance.ResponseBType = value

value = instance.ResponseBType
```

### C#

```csharp
System.int ResponseBType {get; set;}
```

### C++/CLI

```cpp
property System.int ResponseBType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second response user control as defined by [swUserMessageBarResponseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserMessageBarResponseType_e.html)

## VBA Syntax

See [MessageBarDefinition::ResponseBType](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition~ResponseBType.html).

## Remarks

Default value of this property is swUserMessageBarResponseType_e.swUserMessageBarResponseType_None.

## See Also

[IMessageBarDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html)
[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
