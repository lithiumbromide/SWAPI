---
title: "IsEnvelope Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsEnvelope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsEnvelope.html"
---

# IsEnvelope Method (IComponent2)

Gets whether this component is an envelope.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsEnvelope() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsEnvelope()
```

### C#

```csharp
System.bool IsEnvelope()
```

### C++/CLI

```cpp
System.bool IsEnvelope();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is an envelope, false if not

## VBA Syntax

See [Component2::IsEnvelope](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsEnvelope.html).

## Examples

[Change Component to Envelope (C#)](Change_Component_to_Envelope_Example_CSharp.htm)
[Change Component to Envelope (VB.NET)](Change_Component_to_Envelope_Example_VBNET.htm)
[Change Component to Envelope (VBA)](Change_Component_to_Envelope_Example_VB.htm)

## Remarks

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
