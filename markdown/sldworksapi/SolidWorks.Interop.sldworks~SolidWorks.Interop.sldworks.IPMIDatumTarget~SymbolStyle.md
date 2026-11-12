---
title: "SymbolStyle Property (IPMIDatumTarget)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumTarget"
member: "SymbolStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~SymbolStyle.html"
---

# SymbolStyle Property (IPMIDatumTarget)

Gets the symbol style of this PMI datum target.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property SymbolStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumTarget
Dim value As System.Integer

instance.SymbolStyle = value

value = instance.SymbolStyle
```

### C#

```csharp
System.int SymbolStyle {get; set;}
```

### C++/CLI

```cpp
property System.int SymbolStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Symbol style as defined in [swPMIDatumTargetSymbolStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumTargetSymbolStyle_e.html)

## VBA Syntax

See [PMIDatumTarget::SymbolStyle](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumTarget~SymbolStyle.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.html)
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
