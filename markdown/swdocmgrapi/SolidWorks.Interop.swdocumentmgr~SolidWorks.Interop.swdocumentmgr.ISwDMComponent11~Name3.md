---
title: "Name3 Property (ISwDMComponent11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent11"
member: "Name3"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11~Name3.html"
---

# Name3 Property (ISwDMComponent11)

Gets the full name of this component

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name3 As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent11
Dim value As System.String

value = instance.Name3
```

### C#

```csharp
System.string Name3 {get;}
```

### C++/CLI

```cpp
property System.String^ Name3 {
   System.String^ get();
}
```

### Property Value

Full name of component

## VBA Syntax

See [SwDMComponent11::Name3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent11~Name3.html).

## Examples

See the [ISwDMComponent11](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.html) examples.

## Remarks

This property returns the component name appended with an index in the format, "component-1".

## See Also

[ISwDMComponent11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.html)
[ISwDMComponent11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP0
