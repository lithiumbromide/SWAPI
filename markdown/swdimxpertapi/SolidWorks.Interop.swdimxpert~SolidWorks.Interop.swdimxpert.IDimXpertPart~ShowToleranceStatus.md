---
title: "ShowToleranceStatus Property (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "ShowToleranceStatus"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~ShowToleranceStatus.html"
---

# ShowToleranceStatus Property (IDimXpertPart)

Gets and sets whether tolerance status is displayed in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowToleranceStatus As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As System.Boolean

instance.ShowToleranceStatus = value

value = instance.ShowToleranceStatus
```

### C#

```csharp
System.bool ShowToleranceStatus {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowToleranceStatus {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if tolerance status is displayed; false if not

## VBA Syntax

See [DimXpertPart::ShowToleranceStatus](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~ShowToleranceStatus.html).

## Examples

[Auto Dimension Scheme (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
