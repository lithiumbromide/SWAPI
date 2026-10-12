---
title: "DeleteAllTolerances Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "DeleteAllTolerances"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~DeleteAllTolerances.html"
---

# DeleteAllTolerances Method (IDimXpertPart)

Removes all tolerances from the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteAllTolerances() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As System.Boolean

value = instance.DeleteAllTolerances()
```

### C#

```csharp
System.bool DeleteAllTolerances()
```

### C++/CLI

```cpp
System.bool DeleteAllTolerances();
```

### Return Value

True if all tolerances were removed; false if not

## VBA Syntax

See [DimXpertPart::DeleteAllTolerances](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~DeleteAllTolerances.html).

## Examples

[Auto Dimension Scheme (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
