---
title: "IDimXpertGtol Interface"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertGtol"
member: ""
kind: "interface"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertGtol.html"
---

# IDimXpertGtol Interface

Allows you to access a DimXpert Gtol annotation.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDimXpertGtol
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertGtol
```

### C#

```csharp
public interface IDimXpertGtol
```

### C++/CLI

```cpp
public interface class IDimXpertGtol
```

## VBA Syntax

See [DimXpertGtol](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertGtol.html).

## Remarks

[IDimXpertAnnotation](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html) is the parent class of IDimXpertGtol. To access an existing Gtol, call:

1. [IDimXpertAnnotation::GetDisplayEntity](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~GetDisplayEntity.html) to get the SOLIDWORKS annotation object.
2. [IAnnotation::GetSpecificAnnotation](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html) to get the Gtol object.

## Accessors

[IDimXpertPart::InsertGtol](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertGtol.html)

## See Also

[IDimXpertGtol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertGtol_members.html)
[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
